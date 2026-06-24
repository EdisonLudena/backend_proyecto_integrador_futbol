from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from stats.views.health import health_check
from stats.views.auth import RegisterView, LogoutView
from stats.views.user import UserViewSet
from stats.views.suscripcion import SuscripcionViewSet
from stats.views.entidad import EntidadViewSet
from stats.serializers.auth import CustomTokenView

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('subscriptions', SuscripcionViewSet, basename='subscription')
router.register('entities', EntidadViewSet, basename='entity')

urlpatterns = [
    path('health/',             health_check),
    path('auth/register/',      RegisterView.as_view()),
    path('auth/login/',         CustomTokenView.as_view()),
    path('auth/token/refresh/', TokenRefreshView.as_view()),
    path('auth/token/verify/',  TokenVerifyView.as_view()),
    path('auth/logout/',        LogoutView.as_view()),
    path('', include(router.urls)),
]