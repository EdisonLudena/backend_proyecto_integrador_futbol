from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from stats.models.jugador_posicion import JugadorPosicion
from stats.serializers.jugador_posicion import JugadorPosicionSerializer
from stats.filters import JugadorPosicionFilter

class JugadorPosicionViewSet(viewsets.ModelViewSet):
    queryset = JugadorPosicion.objects.all()
    serializer_class = JugadorPosicionSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = JugadorPosicionFilter