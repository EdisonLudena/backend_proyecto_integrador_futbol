import uuid
from django.db import models
from django.db.models import Q
from django.core.validators import MinValueValidator, MaxValueValidator
from stats.models import Categoria, Jugador, Sede
from stats.models.partido import Partido

class EvaluacionPostPartido(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE, related_name='evaluaciones_post_partido', db_column='partido_id')
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE, related_name='evaluaciones_post_partido', db_column='jugador_id')
    calificacion = models.DecimalField(
        max_digits=3, 
        decimal_places=1,
        validators=[MinValueValidator(1.0), MaxValueValidator(10.0)]
    )
    puntos_positivos = models.TextField(null=True, blank=True)
    puntos_a_mejorar = models.TextField(null=True, blank=True)
    es_visible_jugador = models.BooleanField(default=False)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'evaluacion_post_partido'
        constraints = [
            models.UniqueConstraint(
                fields=['partido', 'jugador'],
                name='unique_partido_jugador_evaluacion'
            ),
            models.CheckConstraint(
                condition=Q(calificacion__gte=1.0) & Q(calificacion__lte=10.0),
                name='chk_evaluacion_calificacion_range'
            )
        ]
