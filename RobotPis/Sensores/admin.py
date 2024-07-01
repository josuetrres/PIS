from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(SensorTemperatura)
admin.site.register(SensorPeso)
admin.site.register(SensorGPS)
admin.site.register(SensorProximidad)
