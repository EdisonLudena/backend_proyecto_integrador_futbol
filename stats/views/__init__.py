from .health import health_check
from .auth import RegisterView, LogoutView
from .user import UserViewSet
from .jugador import JugadorViewSet
from .prospecto_seguimiento import ProspectoSeguimientoViewSet
from .categoria import CategoriaViewSet
from .sede import SedeViewSet
from .posicion import PosicionViewSet
from .reporte_scouting import ReporteScoutingViewSet
from .metrica_tecnica import MetricaTecnicaViewSet
from .metrica_tactica import MetricaTacticaViewSet
from .valoracion_economica import ValoracionEconomicaViewSet
from .partido import PartidoViewSet
from .alineacion import AlineacionViewSet
from .evento_live import EventoLiveViewSet
from .evaluacion_post_partido import EvaluacionPostPartidoViewSet
