import uuid
from django.db import models
from django.db.models import F
from django.db.models.functions import Least, Greatest
from stats.models.jugador import Jugador
from stats.models.partido import Partido
from stats.models.posicion import Posicion

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
