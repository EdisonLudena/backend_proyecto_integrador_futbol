from django.contrib import admin
from stats.models.entidad import Entidad

@admin.register(Entidad)
class EntidadAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre_entidad', 'ciudad', 'pais', 'estado', 'creado_en']
    list_filter = ['estado', 'pais', 'ciudad']
    search_fields = ['nombre_entidad', 'telefono_contacto']
    raw_id_fields = ['usuario']