from django.core.management.base import BaseCommand
from django.utils import timezone
from dashboard.models import Station, SensorData
import random

class Command(BaseCommand):
    help = 'Generates random sensor data for each station'

    def handle(self, *args, **options):
        stations = Station.objects.all()

        for station in stations:
            SensorData.objects.create(
                station=station,
                timestamp=timezone.now(),
                temperature=random.uniform(20, 40),
                humidity=random.uniform(50, 80),
            )

        self.stdout.write(self.style.SUCCESS('Sensor data generation complete!'))