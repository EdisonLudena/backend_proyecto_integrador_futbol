from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from stats.models.reporte_scouting import ReporteScouting
from stats.serializers.reporte_scouting import ReporteScoutingSerializer

class ReporteScoutingViewSet(viewsets.ModelViewSet):
    queryset = ReporteScouting.objects.all()
    serializer_class = ReporteScoutingSerializer
    permission_classes = [IsAuthenticated]
