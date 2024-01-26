from django.db import models

class Station(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('inactive', 'Inactive')])
    last_seen = models.DateTimeField(auto_now=True)

class SensorData(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    temperature = models.FloatField()
    humidity = models.FloatField()

