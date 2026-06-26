from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from stats.models.valoracion_economica import ValoracionEconomica
from stats.serializers.valoracion_economica import ValoracionEconomicaSerializer

class ValoracionEconomicaViewSet(viewsets.ModelViewSet):
    queryset = ValoracionEconomica.objects.all()
    serializer_class = ValoracionEconomicaSerializer
    permission_classes = [IsAuthenticated]
