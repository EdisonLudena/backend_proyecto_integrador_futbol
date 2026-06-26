from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from stats.models.sede import Sede
from stats.serializers.sede import SedeSerializer

class SedeViewSet(viewsets.ModelViewSet):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer
    permission_classes = [AllowAny]
