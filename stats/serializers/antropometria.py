from rest_framework import serializers
from stats.models.antropometria import HistorialAntropometrico

class HistorialAntropometricoSerializer(serializers.ModelSerializer):
    imc = serializers.DecimalField(max_digits=5, decimal_places=2, read_only=True)

    class Meta:
        model = HistorialAntropometrico
        fields = [
            'id', 'jugador', 'peso_kg', 'altura_cm', 'grasa_corporal', 
            'masa_muscular', 'imc', 'fecha_toma', 'observaciones'
        ]
        read_only_fields = ['id']