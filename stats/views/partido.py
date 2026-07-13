from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from stats.models.partido import Partido
from stats.serializers.partido import PartidoSerializer

class PartidoViewSet(viewsets.ModelViewSet):
    queryset = Partido.objects.all()
    serializer_class = PartidoSerializer
    permission_classes = [AllowAny]
