from .auth import CustomTokenSerializer, CustomTokenView
from .user import (
    RegisterSerializer,
    UserSerializer,
    UserProfileSerializer,
    ChangePasswordSerializer,
)

from .contrato import ContratoInternoSerializer
from .salud import AntecedentesSaludSerializer
from .antropometria import HistorialAntropometricoSerializer
from .rendimiento import TestRendimientoSerializer
from .lesion import LesionRegistroSerializer, SesionRehabilitacionSerializer
from .dieta import PlanAlimenticioSerializer
from .prospecto import ProspectoSeguimientoSerializer
from .suscripcion import SuscripcionSerializer
from .entidad import EntidadSerializer
from .sede import SedeSerializer
from .categoria import CategoriaSerializer
from .posicion import PosicionSerializer
from .jugador import JugadorSerializer
from .jugador_posicion import JugadorPosicionSerializer
from .representante import RepresentanteSerializer
