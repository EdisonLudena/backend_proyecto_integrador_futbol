from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from stats.models.jugador import Jugador
from stats.serializers.jugador import JugadorSerializer

class JugadorViewSet(viewsets.ModelViewSet):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer
    permission_classes = [AllowAny]
