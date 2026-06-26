from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from stats.models.evento_live import EventoLive
from stats.serializers.evento_live import EventoLiveSerializer

class EventoLiveViewSet(viewsets.ModelViewSet):
    queryset = EventoLive.objects.all()
    serializer_class = EventoLiveSerializer
    permission_classes = [IsAuthenticated]
