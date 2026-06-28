# stats/models/antropometria.py
import uuid
from django.db import models
from django.utils import timezone

class HistorialAntropometrico(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    jugador = models.ForeignKey('Jugador', on_delete=models.CASCADE, related_name='historial_antropometrico')
    peso_kg = models.DecimalField(max_digits=5, decimal_places=2)
    altura_cm = models.DecimalField(max_digits=5, decimal_places=2)
    grasa_corporal = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    masa_muscular = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    fecha_toma = models.DateField(default=timezone.now)
    observaciones = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'historial_antropometrico'
        ordering = ['-fecha_toma']

    @property
    def imc(self):
        if self.altura_cm > 0:
            altura_m = float(self.altura_cm) / 100.0
            return round(float(self.peso_kg) / (altura_m * altura_m), 2)
        return 0.0

    def __str__(self):
        return f"{self.jugador} - {self.fecha_toma}"