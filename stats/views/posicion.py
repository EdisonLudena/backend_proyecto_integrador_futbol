from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from stats.models.posicion import Posicion
from stats.serializers.posicion import PosicionSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from stats.models.posicion import Posicion
from stats.serializers.posicion import PosicionSerializer
from stats.filters import PosicionFilter
from stats.pagination import StandardPagination
from stats.permissions import IsStaffOrReadOnly  # <-- Tu clase de permisos personalizados

class PosicionViewSet(viewsets.ModelViewSet):
    queryset = Posicion.objects.all()
    serializer_class = PosicionSerializer
    permission_classes = [AllowAny]
    permission_classes = [IsStaffOrReadOnly]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PosicionFilter
    search_fields = ['nombre_posicion', 'abreviatura']
    ordering_fields = ['zona', 'nombre_posicion']
    ordering = ['zona', 'nombre_posicion']
