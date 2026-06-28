from rest_framework import serializers
from stats.models.categoria import Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
    nombre_entidad = serializers.ReadOnlyField(source='entidad.nombre_entidad')

    class Meta:
        model = Categoria
        fields = [
            'id', 'entidad', 'nombre_entidad', 'nombre', 
            'edad_minima', 'edad_maxima', 'genero', 'activo'
        ]
        read_only_fields = ['id']

    def validate(self, data):
        edad_min = data.get('edad_minima')
        edad_max = data.get('edad_maxima')

        if edad_min is not None and edad_max is not None:
            if edad_max < edad_min:
                raise serializers.ValidationError({
                    'edad_maxima': 'La edad máxima no puede ser menor que la edad mínima.'
                })
        return data
