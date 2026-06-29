from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from stats.models.representante import Representante
from stats.serializers.representante import RepresentanteSerializer
from stats.filters import RepresentanteFilter
from stats.pagination import StandardPagination

class RepresentanteViewSet(viewsets.ModelViewSet):
    queryset = Representante.objects.all()
    serializer_class = RepresentanteSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = RepresentanteFilter
    search_fields = ['nombre', 'email', 'telefono']
    ordering_fields = ['nombre', 'parentesco']
    ordering = ['nombre']