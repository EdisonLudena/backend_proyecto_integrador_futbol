from rest_framework import serializers
from stats.models.rendimiento import TestRendimiento

class TestRendimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestRendimiento
        fields = '__all__'
        read_only_fields = ['id']