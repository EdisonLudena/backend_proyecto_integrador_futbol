from rest_framework import serializers
from stats.models.representante import Representante

class RepresentanteSerializer(serializers.ModelSerializer):
    nombre_jugador = serializers.ReadOnlyField(source='jugador.nombres')
    apellido_jugador = serializers.ReadOnlyField(source='jugador.apellidos')

    class Meta:
        model = Representante
        fields = [
            'id', 'jugador', 'nombre_jugador', 'apellido_jugador',
            'nombre', 'telefono', 'email', 'parentesco',
            'es_contacto_emergencia', 'es_agente'
        ]
        read_only_fields = ['id']