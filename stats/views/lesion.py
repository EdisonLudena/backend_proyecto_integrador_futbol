from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from stats.models.lesion import LesionRegistro, SesionRehabilitacion
from stats.serializers.lesion import LesionRegistroSerializer, SesionRehabilitacionSerializer
from stats.pagination import StandardPagination

class LesionRegistroViewSet(viewsets.ModelViewSet):
    queryset = LesionRegistro.objects.prefetch_related('sesiones').all()
    serializer_class = LesionRegistroSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['gravedad', 'activa', 'jugador']
    search_fields = ['descripcion', 'zona_cuerpo']
    ordering_fields = ['fecha_inicio']
    ordering = ['-fecha_inicio']

class SesionRehabilitacionViewSet(viewsets.ModelViewSet):
    queryset = SesionRehabilitacion.objects.all()
    serializer_class = SesionRehabilitacionSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['lesion']
    ordering_fields = ['fecha_sesion']
    ordering = ['-fecha_sesion']