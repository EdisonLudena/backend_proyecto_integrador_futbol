from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from stats.models.rendimiento import TestRendimiento
from stats.serializers.rendimiento import TestRendimientoSerializer
from stats.pagination import StandardPagination

class TestRendimientoViewSet(viewsets.ModelViewSet):
    queryset = TestRendimiento.objects.all()
    serializer_class = TestRendimientoSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['jugador']
    ordering_fields = ['fecha_test', 'velocidad_30m_seg']
    ordering = ['-fecha_test']