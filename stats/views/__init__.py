from .health import health_check
from .auth import RegisterView, LogoutView
from .user import UserViewSet

from .contrato import ContratoInternoViewSet
from .salud import AntecedentesSaludViewSet
from .antropometria import HistorialAntropometricoViewSet
from .rendimiento import TestRendimientoViewSet
from .lesion import LesionRegistroViewSet, SesionRehabilitacionViewSet
from .dieta import PlanAlimenticioViewSet
from .prospecto import ProspectoSeguimientoViewSet