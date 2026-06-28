from rest_framework import serializers
from stats.models.prospecto import ProspectoSeguimiento

class ProspectoSeguimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProspectoSeguimiento
        fields = '__all__'
        read_only_fields = ['id', 'creado_en']