# stats/models/rendimiento.py
import uuid
from django.db import models
from django.utils import timezone

class TestRendimiento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    jugador = models.ForeignKey('Jugador', on_delete=models.CASCADE, related_name='tests_rendimiento')
    velocidad_30m_seg = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    velocidad_60m_seg = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    salto_vertical_cm = models.PositiveSmallIntegerField(null=True, blank=True)
    salto_horizontal_cm = models.PositiveSmallIntegerField(null=True, blank=True)
    resistencia_vo2max = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    resistencia_nivel = models.PositiveSmallIntegerField(null=True, blank=True)
    flexibilidad_cm = models.SmallIntegerField(null=True, blank=True)
    agilidad_seg = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    fecha_test = models.DateField(default=timezone.now)
    observaciones = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'tests_rendimiento'
        ordering = ['-fecha_test']

    def __str__(self):
        return f"Test {self.fecha_test} - {self.jugador}"