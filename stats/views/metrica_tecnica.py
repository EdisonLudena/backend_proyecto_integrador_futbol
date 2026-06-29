from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from stats.models.metrica_tecnica import MetricaTecnica
from stats.serializers.metrica_tecnica import MetricaTecnicaSerializer

class MetricaTecnicaViewSet(viewsets.ModelViewSet):
    queryset = MetricaTecnica.objects.all()
    serializer_class = MetricaTecnicaSerializer
    permission_classes = [IsAuthenticated]
