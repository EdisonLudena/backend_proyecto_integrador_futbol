from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from stats.models.placeholders import Jugador, ProspectoSeguimiento, Categoria, Sede, Posicion
from stats.models.scouting import ReporteScouting, MetricaTecnica, MetricaTactica, ValoracionEconomica
from stats.models.competition import Partido, Alineacion, EventoLive, EvaluacionPostPartido
from stats.serializers.scouting_competition import (
    JugadorSerializer, ProspectoSeguimientoSerializer, CategoriaSerializer,
    SedeSerializer, PosicionSerializer, ReporteScoutingSerializer,
    MetricaTecnicaSerializer, MetricaTacticaSerializer, ValoracionEconomicaSerializer,
    PartidoSerializer, AlineacionSerializer, EventoLiveSerializer,
    EvaluacionPostPartidoSerializer
)

class JugadorViewSet(viewsets.ModelViewSet):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer
    permission_classes = [AllowAny]

class ProspectoSeguimientoViewSet(viewsets.ModelViewSet):
    queryset = ProspectoSeguimiento.objects.all()
    serializer_class = ProspectoSeguimientoSerializer
    permission_classes = [AllowAny]

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [AllowAny]

class SedeViewSet(viewsets.ModelViewSet):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer
    permission_classes = [AllowAny]

class PosicionViewSet(viewsets.ModelViewSet):
    queryset = Posicion.objects.all()
    serializer_class = PosicionSerializer
    permission_classes = [AllowAny]

class ReporteScoutingViewSet(viewsets.ModelViewSet):
    queryset = ReporteScouting.objects.all()
    serializer_class = ReporteScoutingSerializer
    permission_classes = [IsAuthenticated]

class MetricaTecnicaViewSet(viewsets.ModelViewSet):
    queryset = MetricaTecnica.objects.all()
    serializer_class = MetricaTecnicaSerializer
    permission_classes = [IsAuthenticated]

class MetricaTacticaViewSet(viewsets.ModelViewSet):
    queryset = MetricaTactica.objects.all()
    serializer_class = MetricaTacticaSerializer
    permission_classes = [IsAuthenticated]

class ValoracionEconomicaViewSet(viewsets.ModelViewSet):
    queryset = ValoracionEconomica.objects.all()
    serializer_class = ValoracionEconomicaSerializer
    permission_classes = [IsAuthenticated]

class PartidoViewSet(viewsets.ModelViewSet):
    queryset = Partido.objects.all()
    serializer_class = PartidoSerializer
    permission_classes = [IsAuthenticated]

class AlineacionViewSet(viewsets.ModelViewSet):
    queryset = Alineacion.objects.all()
    serializer_class = AlineacionSerializer
    permission_classes = [IsAuthenticated]

class EventoLiveViewSet(viewsets.ModelViewSet):
    queryset = EventoLive.objects.all()
    serializer_class = EventoLiveSerializer
    permission_classes = [IsAuthenticated]

class EvaluacionPostPartidoViewSet(viewsets.ModelViewSet):
    queryset = EvaluacionPostPartido.objects.all()
    serializer_class = EvaluacionPostPartidoSerializer
    permission_classes = [IsAuthenticated]
