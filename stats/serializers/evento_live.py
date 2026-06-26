from rest_framework import serializers
from stats.models.evento_live import EventoLive

class EventoLiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoLive
        fields = '__all__'
