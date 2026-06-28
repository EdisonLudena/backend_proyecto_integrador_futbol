from rest_framework import serializers
from stats.models.sede import Sede

class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields = '__all__'
    nombre_entidad = serializers.ReadOnlyField(source='entidad.nombre_entidad')

    class Meta:
        model = Sede
        fields = [
            'id', 'entidad', 'nombre_entidad', 'nombre_sede', 
            'direccion', 'latitud', 'longitud', 'capacidad', 
            'tipo_superficie'
        ]
        read_only_fields = ['id']

    def validate_capacidad(self, value):
        if value is not NULL and value < 0:
            raise serializers.ValidationError('La capacidad de la sede no puede ser un número negativo.')
        return value
