from .auth import CustomTokenSerializer, CustomTokenView
from .user import RegisterSerializer,UserSerializer,UserProfileSerializer,ChangePasswordSerializer
from .jugador import JugadorSerializer
from .prospecto_seguimiento import ProspectoSeguimientoSerializer
from .categoria import CategoriaSerializer
from .sede import SedeSerializer
from .posicion import PosicionSerializer
from .reporte_scouting import ReporteScoutingSerializer
from .metrica_tecnica import MetricaTecnicaSerializer
from .metrica_tactica import MetricaTacticaSerializer
from .valoracion_economica import ValoracionEconomicaSerializer
from .partido import PartidoSerializer
from .alineacion import AlineacionSerializer
from .evento_live import EventoLiveSerializer
from .evaluacion_post_partido import EvaluacionPostPartidoSerializer

