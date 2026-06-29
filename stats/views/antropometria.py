from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from stats.models.antropometria import HistorialAntropometrico
from stats.serializers.antropometria import HistorialAntropometricoSerializer
from stats.pagination import StandardPagination

class HistorialAntropometricoViewSet(viewsets.ModelViewSet):
    queryset = HistorialAntropometrico.objects.all()
    serializer_class = HistorialAntropometricoSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['jugador']
    ordering_fields = ['fecha_toma', 'peso_kg']
    ordering = ['-fecha_toma']