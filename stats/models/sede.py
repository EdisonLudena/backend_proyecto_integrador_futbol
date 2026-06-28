import uuid
from django.db import models
# Importación directa al archivo físico de Entidad para evitar problemas circulares
from stats.models.entidad import Entidad

class Sede(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    entidad = models.ForeignKey(
        Entidad, 
        on_delete=models.CASCADE, 
        related_name='sedes'
    )
    nombre_sede = models.CharField(max_length=150)
    direccion = models.CharField(max_length=300, blank=True, null=True)
    latitud = models.DecimalField(max_length=9, decimal_places=6, max_digits=9, blank=True, null=True)
    longitud = models.DecimalField(max_length=9, decimal_places=6, max_digits=9, blank=True, null=True)
    capacidad = models.IntegerField(blank=True, null=True)
    tipo_superficie = models.CharField(max_length=50, blank=True, null=True) # Grama natural, Sintética, etc.

    class Meta:
        db_table = 'sedes'
        verbose_name = 'Sede'
        verbose_name_plural = 'Sedes'
        ordering = ['nombre_sede']

    def __str__(self):
        return f"{self.nombre_sede} ({self.entidad.nombre_entidad})"