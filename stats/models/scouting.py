import uuid
import datetime
from django.db import models
from django.db.models import Q, F
from django.db.models.functions import Coalesce
from django.core.validators import MinValueValidator, MaxValueValidator
from stats.models.user import Usuario
from stats.models.placeholders import Jugador, ProspectoSeguimiento

class ReporteScouting(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='reportes_scouting', db_column='usuario_id')
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE, null=True, blank=True, related_name='reportes_scouting', db_column='jugador_id')
    prospecto = models.ForeignKey(ProspectoSeguimiento, on_delete=models.CASCADE, null=True, blank=True, related_name='reportes_scouting', db_column='prospecto_id')
    
    valoracion_estrellas = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comentario_tecnico = models.TextField(null=True, blank=True)
    partido_observado = models.CharField(max_length=200, null=True, blank=True)
    fecha_reporte = models.DateField(default=datetime.date.today)

    class Meta:
        db_table = 'reportes_scouting'
        constraints = [
            models.CheckConstraint(
                condition=Q(jugador__isnull=False) | Q(prospecto__isnull=False),
                name='chk_sujeto_reporte'
            ),
            models.CheckConstraint(
                condition=Q(valoracion_estrellas__gte=1) & Q(valoracion_estrellas__lte=5),
                name='chk_valoracion_estrellas_range'
            )
        ]

class MetricaTecnica(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reporte = models.OneToOneField(ReporteScouting, on_delete=models.CASCADE, related_name='metricas_tecnicas', db_column='reporte_id')
    
    control = models.SmallIntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(100)])
    pase_corto = models.SmallIntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(100)])
    pase_largo = models.SmallIntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(100)])
    tiro = models.SmallIntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(100)])
    regate = models.SmallIntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(100)])
    cabeceo = models.SmallIntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(100)])
    velocidad = models.SmallIntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(100)])
    resistencia = models.SmallIntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(100)])

    puntaje_tecnico = models.GeneratedField(
        expression=(
            Coalesce(F('control'), 0) +
            Coalesce(F('pase_corto'), 0) +
            Coalesce(F('pase_largo'), 0) +
            Coalesce(F('tiro'), 0) +
            Coalesce(F('regate'), 0) +
            Coalesce(F('cabeceo'), 0) +
            Coalesce(F('velocidad'), 0) +
            Coalesce(F('resistencia'), 0)
        ) / 8.0,
        output_field=models.DecimalField(max_digits=5, decimal_places=2),
        db_persist=True
    )

    class Meta:
        db_table = 'metricas_tecnicas'
        constraints = [
            models.CheckConstraint(
                condition=Q(control__isnull=True) | (Q(control__gte=1) & Q(control__lte=100)),
                name='chk_metricas_tecnicas_control'
            ),
            models.CheckConstraint(
                condition=Q(pase_corto__isnull=True) | (Q(pase_corto__gte=1) & Q(pase_corto__lte=100)),
                name='chk_metricas_tecnicas_pase_corto'
            ),
            models.CheckConstraint(
                condition=Q(pase_largo__isnull=True) | (Q(pase_largo__gte=1) & Q(pase_largo__lte=100)),
                name='chk_metricas_tecnicas_pase_largo'
            ),
            models.CheckConstraint(
                condition=Q(tiro__isnull=True) | (Q(tiro__gte=1) & Q(tiro__lte=100)),
                name='chk_metricas_tecnicas_tiro'
            ),
            models.CheckConstraint(
                condition=Q(regate__isnull=True) | (Q(regate__gte=1) & Q(regate__lte=100)),
                name='chk_metricas_tecnicas_regate'
            ),
            models.CheckConstraint(
                condition=Q(cabeceo__isnull=True) | (Q(cabeceo__gte=1) & Q(cabeceo__lte=100)),
                name='chk_metricas_tecnicas_cabeceo'
            ),
            models.CheckConstraint(
                condition=Q(velocidad__isnull=True) | (Q(velocidad__gte=1) & Q(velocidad__lte=100)),
                name='chk_metricas_tecnicas_velocidad'
            ),
            models.CheckConstraint(
                condition=Q(resistencia__isnull=True) | (Q(resistencia__gte=1) & Q(resistencia__lte=100)),
                name='chk_metricas_tecnicas_resistencia'
            ),
        ]

class MetricaTactica(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reporte = models.OneToOneField(ReporteScouting, on_delete=models.CASCADE, related_name='metricas_tacticas', db_column='reporte_id')
    
    ubicacion = models.SmallIntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(100)])
    lectura_juego = models.SmallIntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(100)])
    sacrificio = models.SmallIntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(100)])
    liderazgo = models.SmallIntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(100)])
    presion = models.SmallIntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(100)])
    trabajo_equipo = models.SmallIntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(100)])

    puntaje_tactico = models.GeneratedField(
        expression=(
            Coalesce(F('ubicacion'), 0) +
            Coalesce(F('lectura_juego'), 0) +
            Coalesce(F('sacrificio'), 0) +
            Coalesce(F('liderazgo'), 0) +
            Coalesce(F('presion'), 0) +
            Coalesce(F('trabajo_equipo'), 0)
        ) / 6.0,
        output_field=models.DecimalField(max_digits=5, decimal_places=2),
        db_persist=True
    )

    class Meta:
        db_table = 'metricas_tacticas'
        constraints = [
            models.CheckConstraint(
                condition=Q(ubicacion__isnull=True) | (Q(ubicacion__gte=1) & Q(ubicacion__lte=100)),
                name='chk_metricas_tacticas_ubicacion'
            ),
            models.CheckConstraint(
                condition=Q(lectura_juego__isnull=True) | (Q(lectura_juego__gte=1) & Q(lectura_juego__lte=100)),
                name='chk_metricas_tacticas_lectura_juego'
            ),
            models.CheckConstraint(
                condition=Q(sacrificio__isnull=True) | (Q(sacrificio__gte=1) & Q(sacrificio__lte=100)),
                name='chk_metricas_tacticas_sacrificio'
            ),
            models.CheckConstraint(
                condition=Q(liderazgo__isnull=True) | (Q(liderazgo__gte=1) & Q(liderazgo__lte=100)),
                name='chk_metricas_tacticas_liderazgo'
            ),
            models.CheckConstraint(
                condition=Q(presion__isnull=True) | (Q(presion__gte=1) & Q(presion__lte=100)),
                name='chk_metricas_tacticas_presion'
            ),
            models.CheckConstraint(
                condition=Q(trabajo_equipo__isnull=True) | (Q(trabajo_equipo__gte=1) & Q(trabajo_equipo__lte=100)),
                name='chk_metricas_tacticas_trabajo_equipo'
            ),
        ]

class ValoracionEconomica(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE, related_name='valoraciones_economicas', db_column='jugador_id')
    valor_estimado = models.DecimalField(max_digits=14, decimal_places=2)
    moneda = models.CharField(max_length=5, default='USD')
    fecha_valoracion = models.DateField(default=datetime.date.today)
    metodo_valoracion = models.CharField(max_length=80, null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'valoracion_economica'
