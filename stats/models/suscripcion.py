import uuid
from django.db import models
from django.conf import settings

class Suscripcion(models.Model):
    PLANES = [('Basico', 'Basico'), ('Premium', 'Premium')]
    ESTADOS = [('Activo', 'Activo'), ('Cancelado', 'Cancelado'), ('Vencido', 'Vencido'), ('Suspendido', 'Suspendido')]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='suscripciones')
    plan = models.CharField(max_length=20, choices=PLANES)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Activo')
    fecha_inicio = models.DateField(auto_now_add=True)
    fecha_vencimiento = models.DateField()
    metodo_pago = models.CharField(max_length=50, blank=True, null=True)
    referencia_pago = models.CharField(max_length=100, blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'suscripciones'
        verbose_name = 'Suscripcion'
        verbose_name_plural = 'Suscripciones'
        ordering = ['-creado_en']

    def __str__(self):
        return f"{self.usuario.email} - {self.plan}"