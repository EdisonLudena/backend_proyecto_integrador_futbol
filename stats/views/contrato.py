from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from stats.models.contrato import ContratoInterno
from stats.serializers.contrato import ContratoInternoSerializer
from stats.pagination import StandardPagination

class ContratoInternoViewSet(viewsets.ModelViewSet):
    queryset = ContratoInterno.objects.all()
    serializer_class = ContratoInternoSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['tipo_contrato', 'moneda']
    search_fields = ['descripcion', 'jugador__nombres', 'jugador__apellidos']
    ordering_fields = ['fecha_inicio', 'monto']
    ordering = ['-fecha_inicio']