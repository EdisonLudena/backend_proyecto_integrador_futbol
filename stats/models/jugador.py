import uuid
from django.db import models
from stats.models.entidad import Entidad
from stats.models.categoria import Categoria

class Jugador(models.Model):
    PIES_DOMINANTES = [
        ('Derecho', 'Derecho'),
        ('Izquierdo', 'Izquierdo'),
        ('Ambidiestro', 'Ambidiestro'),
    ]

    ESTADOS = [
        ('Activo', 'Activo'),
        ('Lesionado', 'Lesionado'),
        ('Suspendido', 'Suspendido'),
        ('Inactivo', 'Inactivo'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    entidad = models.ForeignKey(
        Entidad, 
        on_delete=models.CASCADE, 
        related_name='jugadores'
    )
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.SET_NULL, 
        related_name='jugadores', 
        blank=True, 
        null=True
    )
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    foto_url = models.URLField(max_length=500, blank=True, null=True)
    numero_camiseta = models.SmallIntegerField(blank=True, null=True)
    pie_dominante = models.CharField(max_length=15, choices=PIES_DOMINANTES, default='Derecho')
    nacionalidad = models.CharField(max_length=80, blank=True, null=True)
    documento_identidad = models.CharField(max_length=30, unique=True, blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Activo')
    creado_en = models.DateTimeField(auto_now_add=True)

    posiciones = models.ManyToManyField(
        'stats.Posicion',
        through='stats.JugadorPosicion',
        related_name='jugadores'
    )

    class Meta:
        db_table = 'jugadores'
        verbose_name = 'Jugador'
        verbose_name_plural = 'Jugadores'
        ordering = ['apellidos', 'nombres']

    def __str__(self):
        return f"{self.apellidos}, {self.nombres}"