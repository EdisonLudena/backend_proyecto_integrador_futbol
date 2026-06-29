from rest_framework import serializers
from stats.models.contrato import ContratoInterno

class ContratoInternoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContratoInterno
        fields = '__all__'
        read_only_fields = ['id', 'creado_en']