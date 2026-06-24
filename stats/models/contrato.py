# stats/models/contrato.py
import uuid
from django.db import models

class ContratoInterno(models.Model):
    TIPO_CHOICES = [
        ('Beca', 'Beca'),
        ('Profesional', 'Profesional'),
        ('Amateur', 'Amateur'),
        ('Prueba', 'Prueba'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    jugador = models.ForeignKey('Jugador', on_delete=models.CASCADE, related_name='contratos')
    tipo_contrato = models.CharField(max_length=30, choices=TIPO_CHOICES)
    monto = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    moneda = models.CharField(max_length=5, default='USD')
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    archivo_url = models.URLField(max_length=500, null=True, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'contratos_internos'
        ordering = ['-fecha_inicio']

    def __str__(self):
        return f"{self.tipo_contrato} - {self.jugador}"