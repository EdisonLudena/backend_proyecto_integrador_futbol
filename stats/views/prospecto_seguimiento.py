from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from stats.models.prospecto_seguimiento import ProspectoSeguimiento
from stats.serializers.prospecto_seguimiento import ProspectoSeguimientoSerializer

class ProspectoSeguimientoViewSet(viewsets.ModelViewSet):
    queryset = ProspectoSeguimiento.objects.all()
    serializer_class = ProspectoSeguimientoSerializer
    permission_classes = [AllowAny]
