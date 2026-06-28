from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from stats.models.dieta import PlanAlimenticio
from stats.serializers.dieta import PlanAlimenticioSerializer
from stats.pagination import StandardPagination

class PlanAlimenticioViewSet(viewsets.ModelViewSet):
    queryset = PlanAlimenticio.objects.all()
    serializer_class = PlanAlimenticioSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['activo', 'jugador']
    ordering_fields = ['fecha_inicio']
    ordering = ['-fecha_inicio']