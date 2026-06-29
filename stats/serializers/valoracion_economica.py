from rest_framework import serializers
from stats.models.valoracion_economica import ValoracionEconomica

class ValoracionEconomicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValoracionEconomica
        fields = '__all__'
