from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from stats.models.categoria import Categoria
from stats.serializers.categoria import CategoriaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [AllowAny]
