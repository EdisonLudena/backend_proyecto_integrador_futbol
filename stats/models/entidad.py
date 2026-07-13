import uuid
from django.db import models
from django.conf import settings

class Entidad(models.Model):
    ESTADOS = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='entidades'
    )
    nombre_entidad = models.CharField(max_length=150)
    logo_url = models.CharField(max_length=500, blank=True, null=True)
    director_tecnico = models.CharField(max_length=150, blank=True, null=True)
    anio_fundacion = models.IntegerField(blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    pais = models.CharField(max_length=100, default='Ecuador')
    telefono_contacto = models.CharField(max_length=20, blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Activo')
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'entidades'
        verbose_name = 'Entidad'
        verbose_name_plural = 'Entidades'
        ordering = ['nombre_entidad']

    def __str__(self):
        return self.nombre_entidad