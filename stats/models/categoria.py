import uuid
from django.db import models
from stats.models.entidad import Entidad

class Categoria(models.Model):
    GENEROS = [
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('Mixto', 'Mixto'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    entidad = models.ForeignKey(
        Entidad, 
        on_delete=models.CASCADE, 
        related_name='categorias'
    )
    nombre = models.CharField(max_length=100)
    edad_minima = models.SmallIntegerField(blank=True, null=True)
    edad_maxima = models.SmallIntegerField(blank=True, null=True)
    genero = models.CharField(max_length=10, choices=GENEROS, default='Masculino')
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'categorias'
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} - {self.entidad.nombre_entidad}"