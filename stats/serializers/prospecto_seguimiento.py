from rest_framework import serializers
from stats.models.prospecto_seguimiento import ProspectoSeguimiento

class ProspectoSeguimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProspectoSeguimiento
        fields = '__all__'
