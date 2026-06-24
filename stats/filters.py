import django_filters
from stats.models.entidad import Entidad
from stats.models import Suscripcion

class SuscripcionFilter(django_filters.FilterSet):
    referencia_pago = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Suscripcion
        fields = ['plan', 'estado']

class EntidadFilter(django_filters.FilterSet):
    nombre_entidad = django_filters.CharFilter(lookup_expr='icontains')
    ciudad = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Entidad
        fields = ['estado', 'pais']