from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from stats.models.metrica_tactica import MetricaTactica
from stats.serializers.metrica_tactica import MetricaTacticaSerializer

class MetricaTacticaViewSet(viewsets.ModelViewSet):
    queryset = MetricaTactica.objects.all()
    serializer_class = MetricaTacticaSerializer
    permission_classes = [IsAuthenticated]
