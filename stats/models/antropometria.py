import uuid
from django.db import models
from django.db.models import F, ExpressionWrapper
from django.utils import timezone


class HistorialAntropometrico(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    jugador = models.ForeignKey(
        'Jugador',
        on_delete=models.CASCADE,
        related_name='historial_antropometrico'
    )
    peso_kg = models.DecimalField(max_digits=5, decimal_places=2)
    altura_cm = models.DecimalField(max_digits=5, decimal_places=2)
    grasa_corporal = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    masa_muscular = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    imc = models.GeneratedField(
        expression=ExpressionWrapper(
            F('peso_kg') / ((F('altura_cm') / 100.0) * (F('altura_cm') / 100.0)),
            output_field=models.DecimalField(max_digits=5, decimal_places=2)
        ),
        output_field=models.DecimalField(max_digits=5, decimal_places=2),
        db_persist=True
    )
    fecha_toma = models.DateField(default=timezone.now)
    observaciones = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'historial_antropometrico'
        ordering = ['-fecha_toma']

    def __str__(self):
        return f"{self.jugador} - {self.fecha_toma}"
