from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class CustomTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['nombre_completo'] = user.nombre_completo
        token['tipo_usuario'] = user.tipo_usuario
        token['is_staff'] = user.is_staff
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['user_id'] = self.user.id
        data['email'] = self.user.email
        data['nombre_completo'] = self.user.nombre_completo
        data['tipo_usuario'] = self.user.tipo_usuario
        data['is_staff'] = self.user.is_staff
        return data

class CustomTokenView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer