from rest_framework import serializers
from stats.models.metrica_tecnica import MetricaTecnica

class MetricaTecnicaSerializer(serializers.ModelSerializer):
    puntaje_tecnico = serializers.DecimalField(max_digits=5, decimal_places=2, read_only=True)

    class Meta:
        model = MetricaTecnica
        fields = '__all__'
