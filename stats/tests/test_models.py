from django.test import TestCase
from django.db import IntegrityError, transaction
from django.utils import timezone
from decimal import Decimal
from stats.models.user import Usuario
from stats.models.placeholders import Jugador, ProspectoSeguimiento, Categoria, Sede, Posicion
from stats.models.scouting import ReporteScouting, MetricaTecnica, MetricaTactica, ValoracionEconomica
from stats.models.competition import Partido, Alineacion, EventoLive, EvaluacionPostPartido

class FootballModelsTest(TestCase):
    def setUp(self):
        # Create a test User
        self.user = Usuario.objects.create_user(
            email='testcoach@example.com',
            nombre_completo='Test Coach',
            tipo_usuario='Coach',
            password='testpassword123'
        )
        # Create placeholder objects
        self.jugador = Jugador.objects.create(nombre='Lionel Messi')
        self.prospecto = ProspectoSeguimiento.objects.create(nombre='Lamine Yamal')
        self.categoria = Categoria.objects.create(nombre='Sub-20')
        self.sede = Sede.objects.create(nombre='Estadio Monumental')
        self.posicion = Posicion.objects.create(nombre='Extremo Derecho')

    def test_reporte_scouting_creation_and_constraints(self):
        # 1. Successful creation with jugador
        reporte_jugador = ReporteScouting.objects.create(
            usuario=self.user,
            jugador=self.jugador,
            valoracion_estrellas=4,
            comentario_tecnico='Excelente desempeño individual.',
            partido_observado='Barcelona vs Real Madrid'
        )
        self.assertEqual(reporte_jugador.valoracion_estrellas, 4)
        self.assertIsNotNone(reporte_jugador.id)

        # 2. Successful creation with prospecto
        reporte_prospecto = ReporteScouting.objects.create(
            usuario=self.user,
            prospecto=self.prospecto,
            valoracion_estrellas=5,
            comentario_tecnico='Gran promesa, muy veloz.',
            partido_observado='Torneo Juvenil'
        )
        self.assertEqual(reporte_prospecto.valoracion_estrellas, 5)

        # 3. Constraint: At least one (jugador or prospecto) must be set
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                ReporteScouting.objects.create(
                    usuario=self.user,
                    valoracion_estrellas=3,
                    comentario_tecnico='Sin sujeto.'
                )

        # 4. Constraint: Stars must be between 1 and 5
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                ReporteScouting.objects.create(
                    usuario=self.user,
                    jugador=self.jugador,
                    valoracion_estrellas=6
                )

        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                ReporteScouting.objects.create(
                    usuario=self.user,
                    jugador=self.jugador,
                    valoracion_estrellas=0
                )

    def test_metricas_tecnicas_generated_field_and_constraints(self):
        reporte = ReporteScouting.objects.create(
            usuario=self.user,
            jugador=self.jugador,
            valoracion_estrellas=4
        )
        # Create metrics
        metrica = MetricaTecnica.objects.create(
            reporte=reporte,
            control=80,
            pase_corto=90,
            pase_largo=70,
            tiro=85,
            regate=95,
            cabeceo=60,
            velocidad=88,
            resistencia=82
        )
        # Refresh from DB to fetch generated field
        metrica.refresh_from_db()
        
        # Expected average = (80+90+70+85+95+60+88+82)/8 = 650/8 = 81.25
        self.assertEqual(metrica.puntaje_tecnico, Decimal('81.25'))

        # Constraint check: value > 100
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                MetricaTecnica.objects.create(
                    reporte=reporte,
                    control=101
                )

    def test_metricas_tacticas_generated_field_and_constraints(self):
        reporte = ReporteScouting.objects.create(
            usuario=self.user,
            prospecto=self.prospecto,
            valoracion_estrellas=3
        )
        # Create metrics
        metrica = MetricaTactica.objects.create(
            reporte=reporte,
            ubicacion=75,
            lectura_juego=80,
            sacrificio=85,
            liderazgo=60,
            presion=70,
            trabajo_equipo=90
        )
        metrica.refresh_from_db()
        
        # Expected average = (75+80+85+60+70+90)/6 = 460/6 = 76.666... -> 76.67
        self.assertAlmostEqual(float(metrica.puntaje_tactico), 76.67, places=2)

        # Constraint check: value < 1
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                MetricaTactica.objects.create(
                    reporte=reporte,
                    ubicacion=0
                )

    def test_partido_and_alineacion_generated_field_and_constraints(self):
        # Create match
        partido = Partido.objects.create(
            categoria=self.categoria,
            sede=self.sede,
            rival='Club Atlético Rival',
            es_local=True,
            fecha=timezone.now(),
            tipo_partido='Liga',
            goles_favor=2,
            goles_contra=1,
            resultado_final='2-1',
            estado_partido='Finalizado'
        )
        self.assertEqual(partido.rival, 'Club Atlético Rival')

        # Create lineup
        alineacion = Alineacion.objects.create(
            partido=partido,
            jugador=self.jugador,
            es_titular=True,
            posicion_partido=self.posicion,
            minuto_entrada=10,
            minuto_salida=85
        )
        alineacion.refresh_from_db()
        
        # Expected minutes = Least(85, 90) - Greatest(10, 0) = 85 - 10 = 75
        self.assertEqual(alineacion.minutos_jugados, 75)

        # Unique constraint test
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Alineacion.objects.create(
                    partido=partido,
                    jugador=self.jugador,
                    es_titular=False
                )

    def test_evaluacion_post_partido(self):
        partido = Partido.objects.create(
            categoria=self.categoria,
            rival='Club Atlético Rival',
            fecha=timezone.now()
        )
        
        evaluacion = EvaluacionPostPartido.objects.create(
            partido=partido,
            jugador=self.jugador,
            calificacion=Decimal('8.5'),
            puntos_positivos='Excelente control de juego.',
            puntos_a_mejorar='Mejorar la resistencia física.'
        )
        self.assertEqual(evaluacion.calificacion, Decimal('8.5'))

        # Constraint test: > 10.0
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                EvaluacionPostPartido.objects.create(
                    partido=partido,
                    jugador=self.jugador,
                    calificacion=Decimal('10.5')
                )
