import uuid
from django.db import models
from django.db.models import Q, F
from django.db.models.functions import Coalesce
from django.core.validators import MinValueValidator, MaxValueValidator
from stats.models.reporte_scouting import ReporteScouting

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
