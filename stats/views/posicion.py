from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from stats.models.posicion import Posicion
from stats.serializers.posicion import PosicionSerializer

class PosicionViewSet(viewsets.ModelViewSet):
    queryset = Posicion.objects.all()
    serializer_class = PosicionSerializer
    permission_classes = [AllowAny]
