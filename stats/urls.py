from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from stats.views.health import health_check
from stats.views.auth import RegisterView, LogoutView
from stats.views.user import UserViewSet
from stats.serializers.auth import CustomTokenView
from stats.views.scouting_competition import (JugadorViewSet,ProspectoSeguimientoViewSet,CategoriaViewSet,SedeViewSet,PosicionViewSet,ReporteScoutingViewSet,MetricaTecnicaViewSet,MetricaTacticaViewSet,ValoracionEconomicaViewSet,PartidoViewSet,AlineacionViewSet,EventoLiveViewSet,EvaluacionPostPartidoViewSet)


router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('jugadores', JugadorViewSet, basename='jugador')
router.register('prospectos-seguimiento', ProspectoSeguimientoViewSet, basename='prospectoseguimiento')
router.register('categorias', CategoriaViewSet, basename='categoria')
router.register('sedes', SedeViewSet, basename='sede')
router.register('posiciones', PosicionViewSet, basename='posicion')
router.register('reportes-scouting', ReporteScoutingViewSet, basename='reportescouting')
router.register('metricas-tecnicas', MetricaTecnicaViewSet, basename='metricatecnica')
router.register('metricas-tacticas', MetricaTacticaViewSet, basename='metricatactica')
router.register('valoracion-economica', ValoracionEconomicaViewSet, basename='valoracioneconomica')
router.register('partidos', PartidoViewSet, basename='partido')
router.register('alineaciones', AlineacionViewSet, basename='alineacion')
router.register('eventos-live', EventoLiveViewSet, basename='eventolive')
router.register('evaluacion-post-partido', EvaluacionPostPartidoViewSet, basename='evaluacionpostpartido')

urlpatterns = [
    path('health/',             health_check),
    path('auth/register/',      RegisterView.as_view()),
    path('auth/login/',         CustomTokenView.as_view()),
    path('auth/token/refresh/', TokenRefreshView.as_view()),
    path('auth/token/verify/',  TokenVerifyView.as_view()),
    path('auth/logout/',        LogoutView.as_view()),
    path('', include(router.urls)),
]
