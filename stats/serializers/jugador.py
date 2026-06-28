from datetime import date
from rest_framework import serializers
from stats.models.jugador import Jugador

class JugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugador
        fields = '__all__'
    nombre_entidad = serializers.ReadOnlyField(source='entidad.nombre_entidad')
    nombre_categoria = serializers.ReadOnlyField(source='categoria.nombre')

    class Meta:
        model = Jugador
        fields = [
            'id', 'entidad', 'nombre_entidad', 'categoria', 'nombre_categoria',
            'nombres', 'apellidos', 'fecha_nacimiento', 'foto_url',
            'numero_camiseta', 'pie_dominante', 'nacionalidad',
            'documento_identidad', 'estado', 'creado_en'
        ]
        read_only_fields = ['id', 'creado_en']

    def validate_numero_camiseta(self, value):
        if value is not None and (value < 1 or value > 99):
            raise serializers.ValidationError('El número de camiseta debe estar comprendido entre 1 y 99.')
        return value

    def validate_fecha_nacimiento(self, value):
        if value > date.today():
            raise serializers.ValidationError('La fecha de nacimiento no puede ser una fecha futura.')
        return value
