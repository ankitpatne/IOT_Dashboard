from django.contrib import admin
from .models import Station, SensorData

# Register your models here.

admin.site.register(Station)
admin.site.register(SensorData)
