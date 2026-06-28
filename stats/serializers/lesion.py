from rest_framework import serializers
from stats.models.lesion import LesionRegistro, SesionRehabilitacion

class SesionRehabilitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SesionRehabilitacion
        fields = '__all__'
        read_only_fields = ['id']
        
    def validate_dolor_nivel(self, value):
        if value is not None and not (0 <= value <= 10):
            raise serializers.ValidationError("El nivel de dolor debe estar entre 0 y 10.")
        return value

class LesionRegistroSerializer(serializers.ModelSerializer):
    sesiones = SesionRehabilitacionSerializer(many=True, read_only=True)

    class Meta:
        model = LesionRegistro
        fields = '__all__'
        read_only_fields = ['id']