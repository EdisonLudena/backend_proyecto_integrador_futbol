import uuid
from django.db import models
from stats.models.jugador import Jugador
from stats.models.posicion import Posicion

class JugadorPosicion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE, related_name='posiciones_asignadas')
    posicion = models.ForeignKey(Posicion, on_delete=models.CASCADE, related_name='jugadores_asignados')
    es_principal = models.BooleanField(default=False)

    class Meta:
        db_table = 'jugadores_posiciones'
        verbose_name = 'Posición de Jugador'
        verbose_name_plural = 'Posiciones de Jugadores'
        constraints = [
            models.UniqueConstraint(fields=['jugador', 'posicion'], name='unique_jugador_posicion')
        ]

    def __str__(self):
        tipo = "Principal" if self.es_principal else "Secundaria"
        return f"{self.jugador} - {self.posicion} ({tipo})"