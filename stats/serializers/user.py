from rest_framework import serializers
from stats.models.user import Usuario

class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    nombre_completo = serializers.CharField(max_length=150)
    tipo_usuario = serializers.ChoiceField(choices=Usuario.TIPOS_USUARIO)
    password = serializers.CharField(min_length=8, write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate_email(self, value):
        if Usuario.objects.filter(email=value).exists():
            raise serializers.ValidationError('This email is already registered.')
        return value

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password2': 'Passwords do not match.'})
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        return Usuario.objects.create_user(**validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'id', 'email', 'nombre_completo', 'tipo_usuario', 
            'estado', 'is_staff', 'is_active', 'fecha_registro'
        ]
        read_only_fields = ['id', 'fecha_registro']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'email', 'nombre_completo', 'tipo_usuario', 'idioma', 'unidad_medida', 'notificaciones_activas']
        read_only_fields = ['id', 'tipo_usuario']

    def validate_email(self, value):
        request = self.context.get('request')
        if Usuario.objects.filter(email=value).exclude(pk=request.user.pk).exists():
            raise serializers.ValidationError('This email is already in use.')
        return value

class ChangePasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(min_length=8, write_only=True)
    new_password2 = serializers.CharField(write_only=True)

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError('Current password is incorrect.')
        return value

    def validate(self, data):
        if data['new_password'] != data['new_password2']:
            raise serializers.ValidationError({'new_password2': 'Passwords do not match.'})
        return data