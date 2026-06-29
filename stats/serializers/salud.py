from rest_framework import serializers
from stats.models.salud import AntecedentesSalud

class AntecedentesSaludSerializer(serializers.ModelSerializer):
    class Meta:
        model = AntecedentesSalud
        fields = '__all__'
        read_only_fields = ['id', 'actualizado_en']