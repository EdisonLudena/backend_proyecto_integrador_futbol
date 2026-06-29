# stats/models/lesion.py
import uuid
from django.db import models
from django.utils import timezone

class LesionRegistro(models.Model):
    GRAVEDAD_CHOICES = [
        ('Leve', 'Leve'),
        ('Moderada', 'Moderada'),
        ('Grave', 'Grave')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    jugador = models.ForeignKey('Jugador', on_delete=models.CASCADE, related_name='lesiones')
    descripcion = models.TextField()
    zona_cuerpo = models.CharField(max_length=80)
    tipo_lesion = models.CharField(max_length=50, null=True, blank=True)
    gravedad = models.CharField(max_length=20, choices=GRAVEDAD_CHOICES, null=True, blank=True)
    fecha_inicio = models.DateField()
    fecha_alta = models.DateField(null=True, blank=True)
    activa = models.BooleanField(default=True)
    medico_tratante = models.CharField(max_length=150, null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'lesiones_registro'
        ordering = ['-fecha_inicio']

    def __str__(self):
        return f"{self.zona_cuerpo} ({self.gravedad}) - {self.jugador}"


class SesionRehabilitacion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lesion = models.ForeignKey(LesionRegistro, on_delete=models.CASCADE, related_name='sesiones')
    ejercicios_realizados = models.TextField()
    duracion_minutos = models.PositiveSmallIntegerField(null=True, blank=True)
    dolor_nivel = models.PositiveSmallIntegerField(null=True, blank=True) 
    fecha_sesion = models.DateField(default=timezone.now)
    fisioterapeuta = models.CharField(max_length=150, null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'sesiones_rehabilitacion'
        ordering = ['-fecha_sesion']

    def __str__(self):
        return f"Sesión {self.fecha_sesion} - Lesión: {self.lesion.zona_cuerpo}"