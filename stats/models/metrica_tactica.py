import uuid
from django.db import models
from django.db.models import Q, F
from django.db.models.functions import Coalesce
from django.core.validators import MinValueValidator, MaxValueValidator
from stats.models.reporte_scouting import ReporteScouting

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
