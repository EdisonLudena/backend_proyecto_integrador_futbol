from rest_framework import serializers
from stats.models.evaluacion_post_partido import EvaluacionPostPartido

class EvaluacionPostPartidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvaluacionPostPartido
        fields = '__all__'
