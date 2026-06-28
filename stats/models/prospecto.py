# stats/models/prospecto.py
import uuid
from django.db import models
from django.conf import settings

class ProspectoSeguimiento(models.Model):
    ESTADO_CHOICES = [
        ('Seguimiento', 'Seguimiento'),
        ('Contactado', 'Contactado'),
        ('En evaluación', 'En evaluación'),
        ('Oferta enviada', 'Oferta enviada'),
        ('Reclutado', 'Reclutado'),
        ('Descartado', 'Descartado'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='prospectos_seguidos')
    jugador = models.ForeignKey('Jugador', on_delete=models.SET_NULL, null=True, blank=True, related_name='prospectos')
    nombre_jugador = models.CharField(max_length=150, null=True, blank=True)
    equipo_actual = models.CharField(max_length=150, null=True, blank=True)
    posicion = models.ForeignKey('Posicion', on_delete=models.SET_NULL, null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    nacionalidad = models.CharField(max_length=80, null=True, blank=True)
    estado = models.CharField(max_length=30, choices=ESTADO_CHOICES, default='Seguimiento')
    fecha_primer_contacto = models.DateField(null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'prospectos_seguimiento'
        ordering = ['-creado_en']

    def __str__(self):
        return self.nombre_jugador if self.nombre_jugador else f"Prospecto: {self.jugador}"