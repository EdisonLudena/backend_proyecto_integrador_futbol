from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count

from stats.models.entidad import Entidad
from stats.serializers.entidad import EntidadSerializer
from stats.filters import EntidadFilter
from stats.pagination import StandardPagination
from stats.permissions import IsCoachOrReadOnly
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

class EntidadViewSet(viewsets.ModelViewSet):
    queryset = Entidad.objects.all()
    serializer_class = EntidadSerializer
    permission_classes = [IsCoachOrReadOnly]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = EntidadFilter
    search_fields = ['nombre_entidad', 'ciudad', 'telefono_contacto']
    ordering_fields = ['nombre_entidad', 'creado_en']
    ordering = ['nombre_entidad']

    @action(detail=False, methods=['get'], url_path='stats')
    def stats(self, request):
        qs = Entidad.objects.all()
        top_ciudades_qs = qs.values('ciudad').annotate(total=Count('id')).order_by('-total')[:5]
        
        return Response({
            'total_entidades': qs.count(),
            'activas': qs.filter(estado='Activo').count(),
            'inactivas': qs.filter(estado='Inactivo').count(),
            'top_ciudades': list(top_ciudades_qs)
        })

    @action(detail=True, methods=['patch'], url_path='escudo')
    def upload_escudo(self, request, pk=None):
        entidad = self.get_object()
        file = request.FILES.get('escudo')
        if not file:
            return Response({'error': 'No se proporcionó ningún archivo'}, status=400)
            
        path = default_storage.save(f'escudos/{file.name}', ContentFile(file.read()))
        entidad.logo_url = request.build_absolute_uri(default_storage.url(path))
        entidad.save()
        return Response({'badgeUrl': entidad.logo_url})