from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from stats.models import Suscripcion
from stats.serializers.suscripcion import SuscripcionSerializer
from stats.permissions import IsStaffOrReadOnly
from stats.filters import SuscripcionFilter
from stats.pagination import StandardPagination

class SuscripcionViewSet(viewsets.ModelViewSet):
    queryset = Suscripcion.objects.all()
    serializer_class = SuscripcionSerializer
    permission_classes = [IsStaffOrReadOnly]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = SuscripcionFilter
    search_fields = ['usuario__email', 'referencia_pago']
    ordering_fields = ['fecha_vencimiento', 'creado_en']
    ordering = ['-creado_en']

    @action(detail=False, methods=['get'], url_path='stats')
    def stats(self, request):
        qs = Suscripcion.objects.all()
        return Response({
            'total_suscripciones': qs.count(),
            'activas': qs.filter(estado='Activo').count(),
            'canceladas': qs.filter(estado='Cancelado').count(),
            'vencidas': qs.filter(estado='Vencido').count(),
            'premium': qs.filter(plan='Premium', estado='Activo').count(),
            'basico': qs.filter(plan='Basico', estado='Activo').count(),
        })