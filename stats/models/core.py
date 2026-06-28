# stats/models/core.py
import uuid
from django.db import models

class Posicion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre_posicion = models.CharField(max_length=80, unique=True)
    zona = models.CharField(max_length=20, default='Mediocampo')

    class Meta:
        db_table = 'posiciones'

    def __str__(self):
        return self.nombre_posicion


class Jugador(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20, default='Activo')

    class Meta:
        db_table = 'jugadores'

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"