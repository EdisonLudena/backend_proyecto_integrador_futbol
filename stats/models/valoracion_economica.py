import uuid
import datetime
from django.db import models
from stats.models.jugador import Jugador

class ValoracionEconomica(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE, related_name='valoraciones_economicas', db_column='jugador_id')
    valor_estimado = models.DecimalField(max_digits=14, decimal_places=2)
    moneda = models.CharField(max_length=5, default='USD')
    fecha_valoracion = models.DateField(default=datetime.date.today)
    metodo_valoracion = models.CharField(max_length=80, null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'valoracion_economica'
