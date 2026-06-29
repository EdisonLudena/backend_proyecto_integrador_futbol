from rest_framework import serializers
from stats.models.metrica_tactica import MetricaTactica

class MetricaTacticaSerializer(serializers.ModelSerializer):
    puntaje_tactico = serializers.DecimalField(max_digits=5, decimal_places=2, read_only=True)

    class Meta:
        model = MetricaTactica
        fields = '__all__'
