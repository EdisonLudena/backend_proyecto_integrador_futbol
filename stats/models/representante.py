import uuid
from django.db import models
from stats.models.jugador import Jugador

class Representante(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    jugador = models.ForeignKey(
        Jugador, 
        on_delete=models.CASCADE, 
        related_name='representantes'
    )
    nombre = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    parentesco = models.CharField(max_length=50, blank=True, null=True)
    es_contacto_emergencia = models.BooleanField(default=False)
    es_agente = models.BooleanField(default=False)

    class Meta:
        db_table = 'representantes'
        verbose_name = 'Representante'
        verbose_name_plural = 'Representantes'
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} ({self.parentesco or 'Sin parentesco'})"