from django.core.management.base import BaseCommand
import random
from faker import Faker
from dashboard.models import Station, SensorData

class Command(BaseCommand):
    help = 'Populates the database with dummy data'

    def handle(self, *args, **options):
        fake = Faker()

        for i in range(1, 2000):
            station = Station.objects.create(
                name=fake.address(),
                latitude=random.uniform(6.748026, 35.426388),
                longitude=random.uniform(70.009027, 97.226765),
                status=random.choice(['active', 'inactive']),
            )
            for _ in range(10):
                SensorData.objects.create(
                    station=station,
                    temperature=random.uniform(20, 40),
                    humidity=random.uniform(50, 80),
                    timestamp=fake.date_time_between(start_date='-1y', end_date='now', tzinfo=None)
                )

        self.stdout.write(self.style.SUCCESS('Dummy data generation complete!'))