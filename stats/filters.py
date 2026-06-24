import django_filters
from stats.models.entidad import Entidad
from stats.models import Suscripcion
from stats.models.sede import Sede
from stats.models.categoria import Categoria
from stats.models.posicion import Posicion

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

class SedeFilter(django_filters.FilterSet):
    nombre_sede = django_filters.CharFilter(lookup_expr='icontains')
    tipo_superficie = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Sede
        fields = ['entidad', 'tipo_superficie']

class CategoriaFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Categoria
        fields = ['entidad', 'genero', 'activo']

class PosicionFilter(django_filters.FilterSet):
    nombre_posicion = django_filters.CharFilter(lookup_expr='icontains')
    abreviatura = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Posicion
        fields = ['zona']