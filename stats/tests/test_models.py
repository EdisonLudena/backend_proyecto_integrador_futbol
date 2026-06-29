from django.test import TestCase
from django.db import IntegrityError, transaction
from django.utils import timezone
from decimal import Decimal
from stats.models import (
    Usuario,
    Jugador,
    ProspectoSeguimiento,
    Categoria,
    Sede,
    Posicion,
    ReporteScouting,
    MetricaTecnica,
    MetricaTactica,
    ValoracionEconomica,
    Partido,
    Alineacion,
    EventoLive,
    EvaluacionPostPartido,
)
from stats.models.entidad import Entidad


class FootballModelsTest(TestCase):
    def setUp(self):
        self.user = Usuario.objects.create_user(
            email='testcoach@example.com',
            nombre_completo='Test Coach',
            tipo_usuario='Coach',
            password='testpassword123'
        )
        self.entidad = Entidad.objects.create(
            usuario=self.user,
            nombre_entidad='Club Test'
        )
        self.categoria = Categoria.objects.create(
            entidad=self.entidad,
            nombre='Sub-20'
        )
        self.sede = Sede.objects.create(
            entidad=self.entidad,
            nombre_sede='Estadio Monumental'
        )
        self.posicion = Posicion.objects.create(
            nombre_posicion='Extremo Derecho',
            abreviatura='ED',
            zona='Ataque'
        )
        self.jugador = Jugador.objects.create(
            entidad=self.entidad,
            nombres='Lionel',
            apellidos='Messi',
            fecha_nacimiento='1987-06-24'
        )
        self.prospecto = ProspectoSeguimiento.objects.create(
            usuario=self.user,
            nombre_jugador='Lamine Yamal'
        )

    def test_reporte_scouting_creation_and_constraints(self):
        reporte_jugador = ReporteScouting.objects.create(
            usuario=self.user,
            jugador=self.jugador,
            valoracion_estrellas=4,
            comentario_tecnico='Excelente desempeño individual.',
            partido_observado='Barcelona vs Real Madrid'
        )
        self.assertEqual(reporte_jugador.valoracion_estrellas, 4)
        self.assertIsNotNone(reporte_jugador.id)

        reporte_prospecto = ReporteScouting.objects.create(
            usuario=self.user,
            prospecto=self.prospecto,
            valoracion_estrellas=5,
            comentario_tecnico='Gran promesa, muy veloz.',
            partido_observado='Torneo Juvenil'
        )
        self.assertEqual(reporte_prospecto.valoracion_estrellas, 5)

        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                ReporteScouting.objects.create(
                    usuario=self.user,
                    valoracion_estrellas=3,
                    comentario_tecnico='Sin sujeto.'
                )

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
        metrica.refresh_from_db()

        self.assertEqual(metrica.puntaje_tecnico, Decimal('81.25'))

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

        self.assertAlmostEqual(float(metrica.puntaje_tactico), 76.67, places=2)

        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                MetricaTactica.objects.create(
                    reporte=reporte,
                    ubicacion=0
                )

    def test_partido_and_alineacion_generated_field_and_constraints(self):
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

        alineacion = Alineacion.objects.create(
            partido=partido,
            jugador=self.jugador,
            es_titular=True,
            posicion_partido=self.posicion,
            minuto_entrada=10,
            minuto_salida=85
        )
        alineacion.refresh_from_db()

        self.assertEqual(alineacion.minutos_jugados, 75)

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

        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                EvaluacionPostPartido.objects.create(
                    partido=partido,
                    jugador=self.jugador,
                    calificacion=Decimal('10.5')
                )