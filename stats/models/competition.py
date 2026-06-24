import uuid
from django.db import models
from django.db.models import Q, F
from django.db.models.functions import Least, Greatest
from django.core.validators import MinValueValidator, MaxValueValidator
from stats.models.placeholders import Jugador, Categoria, Sede, Posicion

class Partido(models.Model):
    TIPO_CHOICES = [
        ('Liga', 'Liga'),
        ('Copa', 'Copa'),
        ('Amistoso', 'Amistoso'),
        ('Torneo', 'Torneo'),
        ('Playoffs', 'Playoffs')
    ]
    ESTADO_CHOICES = [
        ('Programado', 'Programado'),
        ('En curso', 'En curso'),
        ('Finalizado', 'Finalizado'),
        ('Suspendido', 'Suspendido'),
        ('Aplazado', 'Aplazado')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='partidos', db_column='categoria_id')
    sede = models.ForeignKey(Sede, on_delete=models.SET_NULL, null=True, blank=True, related_name='partidos', db_column='sede_id')
    rival = models.CharField(max_length=150)
    es_local = models.BooleanField(default=True)
    fecha = models.DateTimeField()
    tipo_partido = models.CharField(max_length=30, default='Liga', choices=TIPO_CHOICES)
    goles_favor = models.SmallIntegerField(default=0)
    goles_contra = models.SmallIntegerField(default=0)
    resultado_final = models.CharField(max_length=10, null=True, blank=True)
    estado_partido = models.CharField(max_length=20, default='Programado', choices=ESTADO_CHOICES)
    observaciones = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'partidos'
        constraints = [
            models.CheckConstraint(
                condition=Q(tipo_partido__in=['Liga', 'Copa', 'Amistoso', 'Torneo', 'Playoffs']),
                name='chk_partidos_tipo_partido'
            ),
            models.CheckConstraint(
                condition=Q(estado_partido__in=['Programado', 'En curso', 'Finalizado', 'Suspendido', 'Aplazado']),
                name='chk_partidos_estado_partido'
            )
        ]

class Alineacion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE, related_name='alineaciones', db_column='partido_id')
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE, related_name='alineaciones', db_column='jugador_id')
    es_titular = models.BooleanField(default=True)
    posicion_partido = models.ForeignKey(Posicion, on_delete=models.SET_NULL, null=True, blank=True, related_name='alineaciones', db_column='posicion_partido_id')
    minuto_entrada = models.SmallIntegerField(default=0)
    minuto_salida = models.SmallIntegerField(default=90)
    
    minutos_jugados = models.GeneratedField(
        expression=Least(F('minuto_salida'), 90) - Greatest(F('minuto_entrada'), 0),
        output_field=models.SmallIntegerField(),
        db_persist=True
    )

    class Meta:
        db_table = 'alineaciones'
        constraints = [
            models.UniqueConstraint(
                fields=['partido', 'jugador'],
                name='unique_partido_jugador_alineacion'
            )
        ]

class EventoLive(models.Model):
    TIPO_EVENTO_CHOICES = [
        ('Gol', 'Gol'),
        ('Autogol', 'Autogol'),
        ('Asistencia', 'Asistencia'),
        ('Tarjeta amarilla', 'Tarjeta amarilla'),
        ('Tarjeta roja', 'Tarjeta roja'),
        ('Doble amarilla', 'Doble amarilla'),
        ('Penalti anotado', 'Penalti anotado'),
        ('Penalti fallado', 'Penalti fallado'),
        ('Cambio entrada', 'Cambio entrada'),
        ('Cambio salida', 'Cambio salida'),
        ('Lesion', 'Lesion')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE, related_name='eventos', db_column='partido_id')
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE, related_name='eventos', db_column='jugador_id')
    jugador_secundario = models.ForeignKey(Jugador, on_delete=models.SET_NULL, null=True, blank=True, related_name='eventos_asistidos', db_column='jugador_secundario_id')
    minuto = models.SmallIntegerField()
    tipo_evento = models.CharField(max_length=30, choices=TIPO_EVENTO_CHOICES)
    descripcion = models.CharField(max_length=300, null=True, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'eventos_live'
        constraints = [
            models.CheckConstraint(
                condition=Q(tipo_evento__in=[
                    'Gol', 'Autogol', 'Asistencia',
                    'Tarjeta amarilla', 'Tarjeta roja', 'Doble amarilla',
                    'Penalti anotado', 'Penalti fallado',
                    'Cambio entrada', 'Cambio salida',
                    'Lesion'
                ]),
                name='chk_eventos_live_tipo_evento'
            )
        ]

class EvaluacionPostPartido(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE, related_name='evaluaciones_post_partido', db_column='partido_id')
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE, related_name='evaluaciones_post_partido', db_column='jugador_id')
    calificacion = models.DecimalField(
        max_digits=3, 
        decimal_places=1,
        validators=[MinValueValidator(1.0), MaxValueValidator(10.0)]
    )
    puntos_positivos = models.TextField(null=True, blank=True)
    puntos_a_mejorar = models.TextField(null=True, blank=True)
    es_visible_jugador = models.BooleanField(default=False)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'evaluacion_post_partido'
        constraints = [
            models.UniqueConstraint(
                fields=['partido', 'jugador'],
                name='unique_partido_jugador_evaluacion'
            ),
            models.CheckConstraint(
                condition=Q(calificacion__gte=1.0) & Q(calificacion__lte=10.0),
                name='chk_evaluacion_calificacion_range'
            )
        ]
