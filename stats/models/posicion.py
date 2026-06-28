import uuid
from django.db import models

class Posicion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'posiciones'
    ZONAS = [
        ('Porteria', 'Porteria'),
        ('Defensa', 'Defensa'),
        ('Mediocampo', 'Mediocampo'),
        ('Ataque', 'Ataque'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre_posicion = models.CharField(max_length=80, unique=True)
    abreviatura = models.CharField(max_length=10, blank=True, null=True)
    zona = models.CharField(max_length=20, choices=ZONAS)

    class Meta:
        db_table = 'posiciones'
        verbose_name = 'Posición'
        verbose_name_plural = 'Posiciones'
        ordering = ['zona', 'nombre_posicion']

    def __str__(self):
        return f"{self.nombre_posicion} ({self.abreviatura})"
