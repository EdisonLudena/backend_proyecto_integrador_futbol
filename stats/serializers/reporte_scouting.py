from rest_framework import serializers
from stats.models.reporte_scouting import ReporteScouting

class ReporteScoutingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporteScouting
        fields = '__all__'
