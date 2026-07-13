from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from stats.models.categoria import Categoria
from stats.serializers.categoria import CategoriaSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from stats.models.categoria import Categoria
from stats.serializers.categoria import CategoriaSerializer
from stats.filters import CategoriaFilter
from stats.pagination import StandardPagination

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [AllowAny]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CategoriaFilter
    search_fields = ['nombre', 'genero']
    ordering_fields = ['nombre', 'edad_minima']
    ordering = ['nombre']
