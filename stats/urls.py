from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from stats.views.health import health_check
from stats.views.auth import RegisterView, LogoutView
from stats.views.user import UserViewSet
from stats.serializers.auth import CustomTokenView

from stats.views import (
    ContratoInternoViewSet,
    AntecedentesSaludViewSet,
    HistorialAntropometricoViewSet,
    TestRendimientoViewSet,
    LesionRegistroViewSet,
    SesionRehabilitacionViewSet,
    PlanAlimenticioViewSet,
    ProspectoSeguimientoViewSet
)

router = DefaultRouter()

router.register('users', UserViewSet, basename='user')
router.register('contratos', ContratoInternoViewSet, basename='contrato')
router.register('salud', AntecedentesSaludViewSet, basename='salud')
router.register('antropometria', HistorialAntropometricoViewSet, basename='antropometria')
router.register('rendimiento', TestRendimientoViewSet, basename='rendimiento')
router.register('lesiones', LesionRegistroViewSet, basename='lesion')
router.register('rehabilitacion', SesionRehabilitacionViewSet, basename='rehabilitacion')
router.register('dietas', PlanAlimenticioViewSet, basename='dieta')
router.register('prospectos', ProspectoSeguimientoViewSet, basename='prospecto')

urlpatterns = [
    path('health/', health_check),
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', CustomTokenView.as_view()),
    path('auth/token/refresh/', TokenRefreshView.as_view()),
    path('auth/token/verify/', TokenVerifyView.as_view()),
    path('auth/logout/', LogoutView.as_view()),
    path('', include(router.urls)),
]