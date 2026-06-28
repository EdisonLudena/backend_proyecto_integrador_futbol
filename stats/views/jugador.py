from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from stats.models.jugador import Jugador
from stats.serializers.jugador import JugadorSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from stats.models.jugador import Jugador
from stats.serializers.jugador import JugadorSerializer
from stats.filters import JugadorFilter
from stats.pagination import StandardPagination

class JugadorViewSet(viewsets.ModelViewSet):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer
    permission_classes = [AllowAny]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = JugadorFilter
    search_fields = ['nombres', 'apellidos', 'documento_identidad', 'nacionalidad']
    ordering_fields = ['apellidos', 'nombres', 'fecha_nacimiento', 'numero_camiseta']
    ordering = ['apellidos', 'nombres']
