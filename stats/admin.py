from django.contrib import admin
from stats.models import (
    Jugador, Posicion, ContratoInterno, AntecedentesSalud, 
    HistorialAntropometrico, TestRendimiento, LesionRegistro, 
    SesionRehabilitacion, PlanAlimenticio, ProspectoSeguimiento
)

admin.site.register(Jugador)
admin.site.register(Posicion)

admin.site.register(ContratoInterno)
admin.site.register(AntecedentesSalud)
admin.site.register(HistorialAntropometrico)
admin.site.register(TestRendimiento)
admin.site.register(LesionRegistro)
admin.site.register(SesionRehabilitacion)
admin.site.register(PlanAlimenticio)
admin.site.register(ProspectoSeguimiento)