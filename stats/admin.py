from django.contrib import admin
from stats.models import (
    Usuario, Jugador, ProspectoSeguimiento, Categoria, Sede, Posicion, 
    ReporteScouting, MetricaTecnica, MetricaTactica, ValoracionEconomica, 
    Partido, Alineacion, EventoLive, EvaluacionPostPartido, ContratoInterno, 
    AntecedentesSalud, HistorialAntropometrico, TestRendimiento, LesionRegistro, 
    SesionRehabilitacion, PlanAlimenticio, Suscripcion, Entidad, 
    JugadorPosicion, Representante
)

admin.site.register(ContratoInterno)
admin.site.register(AntecedentesSalud)
admin.site.register(HistorialAntropometrico)
admin.site.register(TestRendimiento)
admin.site.register(LesionRegistro)
admin.site.register(SesionRehabilitacion)
admin.site.register(PlanAlimenticio)
admin.site.register(ProspectoSeguimiento)

admin.site.register(Usuario)
admin.site.register(ReporteScouting)
admin.site.register(MetricaTecnica)
admin.site.register(MetricaTactica)
admin.site.register(ValoracionEconomica)
admin.site.register(Partido)
admin.site.register(Alineacion)
admin.site.register(EventoLive)
admin.site.register(EvaluacionPostPartido)

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

@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
    list_display = ['id', 'apellidos', 'nombres', 'entidad', 'categoria', 'numero_camiseta', 'estado']
    list_filter = ['estado', 'pie_dominante', 'entidad', 'categoria']
    search_fields = ['nombres', 'apellidos', 'documento_identidad']
    raw_id_fields = ['entidad', 'categoria']

@admin.register(JugadorPosicion)
class JugadorPosicionAdmin(admin.ModelAdmin):
    list_display = ['id', 'jugador', 'posicion', 'es_principal']
    list_filter = ['es_principal', 'posicion__zona']
    search_fields = ['jugador__nombres', 'jugador__apellidos', 'posicion__nombre_posicion']
    raw_id_fields = ['jugador', 'posicion']

@admin.register(Representante)
class RepresentanteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'jugador', 'parentesco', 'es_contacto_emergencia', 'es_agente']
    list_filter = ['es_contacto_emergencia', 'es_agente', 'parentesco']
    search_fields = ['nombre', 'email', 'telefono', 'jugador__nombres', 'jugador__apellidos']
    raw_id_fields = ['jugador']