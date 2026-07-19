from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from stats.models.salud import AntecedentesSalud
from stats.serializers.salud import AntecedentesSaludSerializer
from stats.pagination import StandardPagination

class AntecedentesSaludViewSet(viewsets.ModelViewSet):
    queryset = AntecedentesSalud.objects.all()
    serializer_class = AntecedentesSaludSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tipo_sangre', 'jugador']