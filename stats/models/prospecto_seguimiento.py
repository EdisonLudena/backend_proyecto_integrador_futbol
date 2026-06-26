import uuid
from django.db import models

class ProspectoSeguimiento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'prospectos_seguimiento'
