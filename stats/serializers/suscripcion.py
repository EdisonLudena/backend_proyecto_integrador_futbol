from rest_framework import serializers
from stats.models import Suscripcion

class SuscripcionSerializer(serializers.ModelSerializer):
    email_usuario = serializers.ReadOnlyField(source='usuario.email')

    class Meta:
        model = Suscripcion
        fields = [
            'id', 'usuario', 'email_usuario', 'plan', 'estado', 
            'fecha_inicio', 'fecha_vencimiento', 'metodo_pago', 
            'referencia_pago', 'creado_en'
        ]
        read_only_fields = ['id', 'fecha_inicio', 'creado_en']

    def validate(self, data):
        if data['fecha_vencimiento'] <= data.get('fecha_inicio', serializers.DateTimeField().to_internal_value(serializers.DateTimeField().now().date())):
            raise serializers.ValidationError({'fecha_vencimiento': 'La fecha de vencimiento debe ser posterior a la fecha de inicio.'})
        return data