from django.contrib import admin
from stats.models.suscripcion import Suscripcion
from stats.models.entidad import Entidad
from stats.models.sede import Sede
from stats.models.categoria import Categoria
from stats.models.posicion import Posicion


@admin.register(Suscripcion)
class SuscripcionAdmin(admin.ModelAdmin):
    list_display = ['usuario_email', 'plan', 'estado', 'fecha_vencimiento', 'creado_en']
    list_filter = ['plan', 'estado', 'fecha_vencimiento']
    search_fields = ['usuario__email', 'referencia_pago', 'usuario__nombre_completo']
    raw_id_fields = ['usuario']
    date_hierarchy = 'fecha_vencimiento'

    def usuario_email(self, obj):
        return obj.usuario.email
    usuario_email.short_description = 'Usuario'

@admin.register(Entidad)
class EntidadAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre_entidad', 'ciudad', 'pais', 'estado', 'creado_en']
    list_filter = ['estado', 'pais', 'ciudad']
    search_fields = ['nombre_entidad', 'telefono_contacto']
    raw_id_fields = ['usuario']

@admin.register(Sede)
class SedeAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre_sede', 'entidad', 'capacidad', 'tipo_superficie']
    list_filter = ['tipo_superficie', 'entidad']
    search_fields = ['nombre_sede', 'direccion']
    raw_id_fields = ['entidad']

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'entidad', 'edad_minima', 'edad_maxima', 'genero', 'activo']
    list_filter = ['activo', 'genero', 'entidad']
    search_fields = ['nombre']
    raw_id_fields = ['entidad']

@admin.register(Posicion)
class PosicionAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre_posicion', 'abreviatura', 'zona']
    list_filter = ['zona']
    search_fields = ['nombre_posicion', 'abreviatura']