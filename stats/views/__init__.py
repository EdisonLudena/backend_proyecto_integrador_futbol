from .health import health_check
from .auth import RegisterView, LogoutView
from .user import UserViewSet
from .scouting_competition import (
    JugadorViewSet,
    ProspectoSeguimientoViewSet,
    CategoriaViewSet,
    SedeViewSet,
    PosicionViewSet,
    ReporteScoutingViewSet,
    MetricaTecnicaViewSet,
    MetricaTacticaViewSet,
    ValoracionEconomicaViewSet,
    PartidoViewSet,
    AlineacionViewSet,
    EventoLiveViewSet,
    EvaluacionPostPartidoViewSet,
)