from rest_framework import serializers
from stats.models.jugador_posicion import JugadorPosicion

class JugadorPosicionSerializer(serializers.ModelSerializer):
    nombre_jugador = serializers.ReadOnlyField(source='jugador.nombres')
    apellido_jugador = serializers.ReadOnlyField(source='jugador.apellidos')
    nombre_posicion = serializers.ReadOnlyField(source='posicion.nombre_posicion')
    abreviatura_posicion = serializers.ReadOnlyField(source='posicion.abreviatura')

    class Meta:
        model = JugadorPosicion
        fields = [
            'id', 'jugador', 'nombre_jugador', 'apellido_jugador',
            'posicion', 'nombre_posicion', 'abreviatura_posicion', 'es_principal'
        ]
        read_only_fields = ['id']

    def validate(self, data):
        jugador = data.get('jugador')
        es_principal = data.get('es_principal', False)

        if es_principal:
            query = JugadorPosicion.objects.filter(jugador=jugador, es_principal=True)
            if self.instance:
                query = query.exclude(id=self.instance.id)
            if query.exists():
                raise serializers.ValidationError(
                    {'es_principal': 'Este jugador ya tiene una posición principal asignada.'}
                )
        return data