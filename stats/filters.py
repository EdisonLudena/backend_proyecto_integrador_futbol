import django_filters
from stats.models.entidad import Entidad
from stats.models import Suscripcion
from stats.models.sede import Sede
from stats.models.categoria import Categoria
from stats.models.posicion import Posicion
from stats.models.jugador import Jugador    
from stats.models.jugador_posicion import JugadorPosicion
from stats.models.representante import Representante

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

class JugadorFilter(django_filters.FilterSet):
    nombres = django_filters.CharFilter(lookup_expr='icontains')
    apellidos = django_filters.CharFilter(lookup_expr='icontains')
    documento_identidad = django_filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = Jugador
        fields = ['entidad', 'categoria', 'estado', 'pie_dominante']

class JugadorPosicionFilter(django_filters.FilterSet):
    class Meta:
        model = JugadorPosicion
        fields = ['jugador', 'posicion', 'es_principal']

class RepresentanteFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Representante
        fields = ['jugador', 'parentesco', 'es_contacto_emergencia', 'es_agente']