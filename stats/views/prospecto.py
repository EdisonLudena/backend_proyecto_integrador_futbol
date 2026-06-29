from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from stats.models.prospecto import ProspectoSeguimiento
from stats.serializers.prospecto import ProspectoSeguimientoSerializer
from stats.pagination import StandardPagination

class ProspectoSeguimientoViewSet(viewsets.ModelViewSet):
    queryset = ProspectoSeguimiento.objects.all()
    serializer_class = ProspectoSeguimientoSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['estado', 'nacionalidad']
    search_fields = ['nombre_jugador', 'equipo_actual', 'observaciones']
    ordering_fields = ['fecha_primer_contacto', 'creado_en']
    ordering = ['-creado_en']