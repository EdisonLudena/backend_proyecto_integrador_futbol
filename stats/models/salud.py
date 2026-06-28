# stats/models/salud.py
import uuid
from django.db import models

class AntecedentesSalud(models.Model):
    SANGRE_CHOICES = [
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    jugador = models.ForeignKey('Jugador', on_delete=models.CASCADE, related_name='antecedentes_salud')
    tipo_sangre = models.CharField(max_length=5, choices=SANGRE_CHOICES, null=True, blank=True)
    alergias = models.TextField(null=True, blank=True)
    medicamentos_regulares = models.TextField(null=True, blank=True)
    condiciones_cronicas = models.TextField(null=True, blank=True)
    contacto_medico_nombre = models.CharField(max_length=150, null=True, blank=True)
    contacto_medico_tel = models.CharField(max_length=20, null=True, blank=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'antecedentes_salud'

    def __str__(self):
        return f"Salud: {self.jugador}"