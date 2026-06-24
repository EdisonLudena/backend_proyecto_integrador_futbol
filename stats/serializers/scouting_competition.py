from rest_framework import serializers
from stats.models.placeholders import Jugador, ProspectoSeguimiento, Categoria, Sede, Posicion
from stats.models.scouting import ReporteScouting, MetricaTecnica, MetricaTactica, ValoracionEconomica
from stats.models.competition import Partido, Alineacion, EventoLive, EvaluacionPostPartido

class JugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugador
        fields = '__all__'

class ProspectoSeguimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProspectoSeguimiento
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields = '__all__'

class PosicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posicion
        fields = '__all__'

class ReporteScoutingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporteScouting
        fields = '__all__'

class MetricaTecnicaSerializer(serializers.ModelSerializer):
    puntaje_tecnico = serializers.DecimalField(max_digits=5, decimal_places=2, read_only=True)

    class Meta:
        model = MetricaTecnica
        fields = '__all__'

class MetricaTacticaSerializer(serializers.ModelSerializer):
    puntaje_tactico = serializers.DecimalField(max_digits=5, decimal_places=2, read_only=True)

    class Meta:
        model = MetricaTactica
        fields = '__all__'

class ValoracionEconomicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValoracionEconomica
        fields = '__all__'

class PartidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partido
        fields = '__all__'

class AlineacionSerializer(serializers.ModelSerializer):
    minutos_jugados = serializers.IntegerField(read_only=True)

    class Meta:
        model = Alineacion
        fields = '__all__'

class EventoLiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoLive
        fields = '__all__'

class EvaluacionPostPartidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvaluacionPostPartido
        fields = '__all__'
