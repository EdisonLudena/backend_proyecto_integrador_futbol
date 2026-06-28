from django.core.management.base import BaseCommand
from stats.models.posicion import Posicion

class Command(BaseCommand):
    help = 'Siembra las posiciones estándar del fútbol en el catálogo maestro'

    def handle(self, *args, **options):
        posiciones_predeterminadas = [
            # Portería
            {'nombre_posicion': 'Guardameta', 'abreviatura': 'GK', 'zona': 'Porteria'},
            # Defensas
            {'nombre_posicion': 'Defensa Central', 'abreviatura': 'CB', 'zona': 'Defensa'},
            {'nombre_posicion': 'Lateral Izquierdo', 'abreviatura': 'LB', 'zona': 'Defensa'},
            {'nombre_posicion': 'Lateral Derecho', 'abreviatura': 'RB', 'zona': 'Defensa'},
            # Mediocampo
            {'nombre_posicion': 'Mediocampista Defensivo', 'abreviatura': 'CDM', 'zona': 'Mediocampo'},
            {'nombre_posicion': 'Mediocampista Central', 'abreviatura': 'CM', 'zona': 'Mediocampo'},
            {'nombre_posicion': 'Mediocampista Ofensivo', 'abreviatura': 'CAM', 'zona': 'Mediocampo'},
            # Ataque
            {'nombre_posicion': 'Extremo Izquierdo', 'abreviatura': 'LW', 'zona': 'Ataque'},
            {'nombre_posicion': 'Extremo Derecho', 'abreviatura': 'RW', 'zona': 'Ataque'},
            {'nombre_posicion': 'Delantero Centro', 'abreviatura': 'ST', 'zona': 'Ataque'},
        ]

        for pos in posiciones_predeterminadas:
            obj, created = Posicion.objects.get_or_create(
                nombre_posicion=pos['nombre_posicion'],
                defaults={'abreviatura': pos['abreviatura'], 'zona': pos['zona']}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Posición creada: {pos['nombre_posicion']}"))
            else:
                self.stdout.write(self.style.WARNING(f"Posición ya existente: {pos['nombre_posicion']}"))