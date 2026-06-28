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
        # 1. El usuario debe estar autenticado
        if not request.user or not request.user.is_authenticated:
            return False
        
        # 2. Verificamos si tiene una suscripción activa de tipo 'Premium'
        return Suscripcion.objects.filter(
            usuario=request.user,
            plan='Premium',
            estado='Activo',
            fecha_vencimiento__gte=timezone.now().date()
        ).exists()