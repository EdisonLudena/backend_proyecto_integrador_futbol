from rest_framework import serializers
from stats.models.alineacion import Alineacion

class AlineacionSerializer(serializers.ModelSerializer):
    minutos_jugados = serializers.IntegerField(read_only=True)

    class Meta:
        model = Alineacion
        fields = '__all__'
