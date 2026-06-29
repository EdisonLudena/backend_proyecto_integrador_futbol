from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from stats.models.sede import Sede
from stats.serializers.sede import SedeSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from stats.models.sede import Sede
from stats.serializers.sede import SedeSerializer
from stats.filters import SedeFilter
from stats.pagination import StandardPagination

class SedeViewSet(viewsets.ModelViewSet):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer
    permission_classes = [AllowAny]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = SedeFilter
    search_fields = ['nombre_sede', 'direccion', 'tipo_superficie']
    ordering_fields = ['nombre_sede', 'capacidad']
    ordering = ['nombre_sede']
