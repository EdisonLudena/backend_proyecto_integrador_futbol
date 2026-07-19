import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UsuarioManager(BaseUserManager):
    def create_user(self, email, nombre_completo, tipo_usuario, password=None, **extra_fields):
        if not email:
            raise ValueError('El email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            nombre_completo=nombre_completo,
            tipo_usuario=tipo_usuario,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nombre_completo, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, nombre_completo, 'Admin', password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    TIPOS_USUARIO = [('Coach', 'Coach'), ('Scout', 'Scout'), ('Player', 'Player'), ('Admin', 'Admin')]
    ESTADOS = [('Activo', 'Activo'), ('Inactivo', 'Inactivo'), ('Suspendido', 'Suspendido')]
    UNIDADES = [('Metrico', 'Metrico'), ('Imperial', 'Imperial')]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    nombre_completo = models.CharField(max_length=150)
    tipo_usuario = models.CharField(max_length=20, choices=TIPOS_USUARIO)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Activo')
    fecha_registro = models.DateTimeField(auto_now_add=True)
    ultimo_login = models.DateTimeField(null=True, blank=True)
    idioma = models.CharField(max_length=10, default='es')
    unidad_medida = models.CharField(max_length=10, choices=UNIDADES, default='Metrico')
    notificaciones_activas = models.BooleanField(default=True)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre_completo']

    class Meta:
        db_table = 'usuarios'