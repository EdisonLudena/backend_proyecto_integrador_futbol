from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from stats.models.alineacion import Alineacion
from stats.serializers.alineacion import AlineacionSerializer

class AlineacionViewSet(viewsets.ModelViewSet):
    queryset = Alineacion.objects.all()
    serializer_class = AlineacionSerializer
    permission_classes = [IsAuthenticated]
