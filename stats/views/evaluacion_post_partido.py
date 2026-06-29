from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from stats.models.evaluacion_post_partido import EvaluacionPostPartido
from stats.serializers.evaluacion_post_partido import EvaluacionPostPartidoSerializer

class EvaluacionPostPartidoViewSet(viewsets.ModelViewSet):
    queryset = EvaluacionPostPartido.objects.all()
    serializer_class = EvaluacionPostPartidoSerializer
    permission_classes = [IsAuthenticated]
