from rest_framework import serializers
from stats.models.partido import Partido

class PartidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partido
        fields = '__all__'
