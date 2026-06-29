import uuid
import datetime
from django.db import models
from django.db.models import Q
from django.core.validators import MinValueValidator, MaxValueValidator
from stats.models.user import Usuario
from stats.models.jugador import Jugador
from stats.models.prospecto import ProspectoSeguimiento


class ReporteScouting(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='reportes_scouting', db_column='usuario_id')
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE, null=True, blank=True, related_name='reportes_scouting', db_column='jugador_id')
    prospecto = models.ForeignKey(ProspectoSeguimiento, on_delete=models.CASCADE, null=True, blank=True, related_name='reportes_scouting', db_column='prospecto_id')
    valoracion_estrellas = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comentario_tecnico = models.TextField(null=True, blank=True)
    partido_observado = models.CharField(max_length=200, null=True, blank=True)
    fecha_reporte = models.DateField(default=datetime.date.today)

    class Meta:
        db_table = 'reportes_scouting'
        constraints = [
            models.CheckConstraint(
                condition=Q(jugador__isnull=False) | Q(prospecto__isnull=False),
                name='chk_sujeto_reporte'
            ),
            models.CheckConstraint(
                condition=Q(valoracion_estrellas__gte=1) & Q(valoracion_estrellas__lte=5),
                name='chk_valoracion_estrellas_range'
            )
        ]
