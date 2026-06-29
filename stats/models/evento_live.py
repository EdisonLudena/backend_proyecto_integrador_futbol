import uuid
from django.db import models
from django.db.models import Q
from stats.models.jugador import Jugador
from stats.models.partido import Partido


class EventoLive(models.Model):
    TIPO_EVENTO_CHOICES = [
        ('Gol', 'Gol'),
        ('Autogol', 'Autogol'),
        ('Asistencia', 'Asistencia'),
        ('Tarjeta amarilla', 'Tarjeta amarilla'),
        ('Tarjeta roja', 'Tarjeta roja'),
        ('Doble amarilla', 'Doble amarilla'),
        ('Penalti anotado', 'Penalti anotado'),
        ('Penalti fallado', 'Penalti fallado'),
        ('Cambio entrada', 'Cambio entrada'),
        ('Cambio salida', 'Cambio salida'),
        ('Lesion', 'Lesion'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE, related_name='eventos', db_column='partido_id')
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE, related_name='eventos', db_column='jugador_id')
    jugador_secundario = models.ForeignKey(Jugador, on_delete=models.SET_NULL, null=True, blank=True, related_name='eventos_asistidos', db_column='jugador_secundario_id')
    minuto = models.SmallIntegerField()
    tipo_evento = models.CharField(max_length=30, choices=TIPO_EVENTO_CHOICES)
    descripcion = models.CharField(max_length=300, null=True, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'eventos_live'
        constraints = [
            models.CheckConstraint(
                condition=Q(tipo_evento__in=[
                    'Gol', 'Autogol', 'Asistencia',
                    'Tarjeta amarilla', 'Tarjeta roja', 'Doble amarilla',
                    'Penalti anotado', 'Penalti fallado',
                    'Cambio entrada', 'Cambio salida',
                    'Lesion'
                ]),
                name='chk_eventos_live_tipo_evento'
            )
        ]
