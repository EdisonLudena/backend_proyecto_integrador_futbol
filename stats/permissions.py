from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.utils import timezone
from stats.models.suscripcion import Suscripcion


class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return bool(request.user and request.user.is_authenticated)
        return bool(request.user and request.user.is_staff)
    
class HasPremiumSubscription(BasePermission):
    def has_permission(self, request, view):    
    
        if not request.user or not request.user.is_authenticated:
            return False
        
        
        return Suscripcion.objects.filter(
            usuario=request.user,
            plan='Premium',
            estado='Activo',
            fecha_vencimiento__gte=timezone.now().date()
        ).exists()
    
class IsCoach(BasePermission):
    """Solo usuarios con tipo_usuario == 'Coach' pueden escribir."""
    message = 'Solo los usuarios de tipo Coach pueden realizar esta acción.'

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if request.method in SAFE_METHODS:
            return True
        return request.user.tipo_usuario == 'Coach'


class IsCoachOrReadOnly(BasePermission):
    """Permite lectura pública y escritura solo para coaches autenticados."""
    message = 'Solo los usuarios de tipo Coach pueden realizar esta acción.'

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if not request.user or not request.user.is_authenticated:
            return False
        return request.user.tipo_usuario == 'Coach'
