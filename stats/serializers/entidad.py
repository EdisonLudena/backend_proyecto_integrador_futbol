from rest_framework import serializers
from stats.models.entidad import Entidad

class EntidadSerializer(serializers.ModelSerializer):
    email_creador = serializers.ReadOnlyField(source='usuario.email')

    class Meta:
        model = Entidad
        fields = [
            'id', 'usuario', 'email_creador', 'nombre_entidad',
            'director_tecnico', 'anio_fundacion',
            'logo_url', 'ciudad', 'pais', 'telefono_contacto',
            'estado', 'creado_en'
        ]
        read_only_fields = ['id', 'creado_en']

    def validate_nombre_entidad(self, value):
        usuario_id = self.initial_data.get('usuario')
        qs = Entidad.objects.filter(nombre_entidad__iexact=value, usuario_id=usuario_id)
        
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
            
        if qs.exists():
            raise serializers.ValidationError('Ya tienes una entidad o club registrado con este nombre exacto.')
        return value