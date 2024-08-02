from django.db import models

# Create your models here.

class Datos (models.Model):
    radar_distancia = models.FloatField()
    radar_angulo = models.IntegerField()
    temperatura = models.FloatField()
    humedad = models.FloatField()
    peso = models.FloatField()
    gps_latitud = models.FloatField()
    gps_longitud = models.FloatField()
    gps_altitud = models.FloatField()
    gps_velocidad = models.FloatField()
    
