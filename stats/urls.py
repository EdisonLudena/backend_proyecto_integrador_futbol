from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from stats.views.health import health_check
from stats.views.auth import RegisterView, LogoutView
from stats.serializers.auth import CustomTokenView


from stats.views import (
    UserViewSet,
    SuscripcionViewSet,
    EntidadViewSet,
    SedeViewSet,
    CategoriaViewSet,
    PosicionViewSet,
    JugadorViewSet,
    JugadorPosicionViewSet,
    RepresentanteViewSet,
    ProspectoSeguimientoViewSet,
    ReporteScoutingViewSet,
    MetricaTecnicaViewSet,
    MetricaTacticaViewSet,
    ValoracionEconomicaViewSet,
    PartidoViewSet,
    AlineacionViewSet,
    EventoLiveViewSet,
    EvaluacionPostPartidoViewSet,
    ContratoInternoViewSet,
    AntecedentesSaludViewSet,
    HistorialAntropometricoViewSet,
    TestRendimientoViewSet,
    LesionRegistroViewSet,
    SesionRehabilitacionViewSet,
    PlanAlimenticioViewSet
)

router = DefaultRouter()

router.register('users', UserViewSet, basename='user')
router.register('suscripciones', SuscripcionViewSet, basename='suscripcion')
router.register('entidades', EntidadViewSet, basename='entidad')
router.register('equipos', EntidadViewSet, basename='equipo')
router.register('sedes', SedeViewSet, basename='sede')
router.register('categorias', CategoriaViewSet, basename='categoria')
router.register('torneos', CategoriaViewSet, basename='torneo')
router.register('posiciones', PosicionViewSet, basename='posicion')
router.register('jugadores', JugadorViewSet, basename='jugador')
router.register('jugador-posiciones', JugadorPosicionViewSet, basename='jugador-posicion')
router.register('representantes', RepresentanteViewSet, basename='representante')
router.register('prospectos-seguimiento', ProspectoSeguimientoViewSet, basename='prospectoseguimiento')
router.register('reportes-scouting', ReporteScoutingViewSet, basename='reportescouting')
router.register('metricas-tecnicas', MetricaTecnicaViewSet, basename='metricatecnica')
router.register('metricas-tacticas', MetricaTacticaViewSet, basename='metricatactica')
router.register('valoracion-economica', ValoracionEconomicaViewSet, basename='valoracioneconomica')
router.register('partidos', PartidoViewSet, basename='partido')
router.register('matches', PartidoViewSet, basename='match')
router.register('alineaciones', AlineacionViewSet, basename='alineacion')
router.register('eventos-live', EventoLiveViewSet, basename='eventolive')
router.register('evaluacion-post-partido', EvaluacionPostPartidoViewSet, basename='evaluacionpostpartido')
router.register('contratos', ContratoInternoViewSet, basename='contrato')
router.register('salud', AntecedentesSaludViewSet, basename='salud')
router.register('antropometria', HistorialAntropometricoViewSet, basename='antropometria')
router.register('rendimiento', TestRendimientoViewSet, basename='rendimiento')
router.register('lesiones', LesionRegistroViewSet, basename='lesion')
router.register('rehabilitacion', SesionRehabilitacionViewSet, basename='rehabilitacion')
router.register('dietas', PlanAlimenticioViewSet, basename='dieta')

urlpatterns = [
    path('health/', health_check),
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', CustomTokenView.as_view()),
    path('auth/token/refresh/', TokenRefreshView.as_view()),
    path('auth/token/verify/', TokenVerifyView.as_view()),
    path('auth/logout/', LogoutView.as_view()),
    path('', include(router.urls)),
]