import uuid
from django.db import models
from django.db.models import Q
from stats.models.categoria import Categoria
from stats.models.sede import Sede

class Partido(models.Model):
    TIPO_CHOICES = [
        ('Liga', 'Liga'),
        ('Copa', 'Copa'),
        ('Amistoso', 'Amistoso'),
        ('Torneo', 'Torneo'),
        ('Playoffs', 'Playoffs')
    ]
    ESTADO_CHOICES = [
        ('Programado', 'Programado'),
        ('En curso', 'En curso'),
        ('Finalizado', 'Finalizado'),
        ('Suspendido', 'Suspendido'),
        ('Aplazado', 'Aplazado')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='partidos', db_column='categoria_id')
    sede = models.ForeignKey(Sede, on_delete=models.SET_NULL, null=True, blank=True, related_name='partidos', db_column='sede_id')
    equipo_local = models.CharField(max_length=150, default='Local')
    equipo_visitante = models.CharField(max_length=150, default='Visitante')
    fecha = models.DateTimeField()
    tipo_partido = models.CharField(max_length=30, default='Liga', choices=TIPO_CHOICES)
    goles_favor = models.SmallIntegerField(default=0)
    goles_contra = models.SmallIntegerField(default=0)
    resultado_final = models.CharField(max_length=10, null=True, blank=True)
    estado_partido = models.CharField(max_length=20, default='Programado', choices=ESTADO_CHOICES)
    observaciones = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'partidos'
        constraints = [
            models.CheckConstraint(
                condition=Q(tipo_partido__in=['Liga', 'Copa', 'Amistoso', 'Torneo', 'Playoffs']),
                name='chk_partidos_tipo_partido'
            ),
            models.CheckConstraint(
                condition=Q(estado_partido__in=['Programado', 'En curso', 'Finalizado', 'Suspendido', 'Aplazado']),
                name='chk_partidos_estado_partido'
            )
        ]
