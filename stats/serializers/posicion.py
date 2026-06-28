from rest_framework import serializers
from stats.models.posicion import Posicion

class PosicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posicion
        fields = '__all__'
        fields = ['id', 'nombre_posicion', 'abreviatura', 'zona']
        read_only_fields = ['id']
