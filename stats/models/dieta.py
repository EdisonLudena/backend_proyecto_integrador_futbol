# stats/models/dieta.py
import uuid
from django.db import models
from django.utils import timezone

class PlanAlimenticio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    jugador = models.ForeignKey('Jugador', on_delete=models.CASCADE, related_name='planes_alimenticios')
    descripcion_dieta = models.TextField(null=True, blank=True)
    calorias_totales = models.PositiveSmallIntegerField(null=True, blank=True)
    proteina_gr = models.PositiveSmallIntegerField(null=True, blank=True)
    carbohidratos_gr = models.PositiveSmallIntegerField(null=True, blank=True)
    grasas_gr = models.PositiveSmallIntegerField(null=True, blank=True)
    hidratacion_ml = models.PositiveSmallIntegerField(null=True, blank=True)
    fecha_inicio = models.DateField(default=timezone.now)
    fecha_fin = models.DateField(null=True, blank=True)
    nutricionista = models.CharField(max_length=150, null=True, blank=True)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'planes_alimenticios'
        ordering = ['-fecha_inicio']

    def __str__(self):
        return f"Plan de Dieta - {self.jugador}"