from django.db import models

# Create your models here.
class Sensor(models.Model):
    imagen = models.URLField(max_length=200, null=True,blank=True)
    nombre = models.CharField(max_length=50)
    VOLTAJE = models.DecimalField(max_digits=5, decimal_places=2)
    CORRIENTE = models.DecimalField(max_digits=5, decimal_places=2)
    unidadMedida = models.CharField(max_length=50)
    estado = models.BooleanField(default=False)
    rangoOperacion = models.CharField(max_length=50)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nombre
    
class SensorTemperatura(Sensor):
    def definirPosicionInicial(self):
        self.estado = False
    
    def medirTemperatura(self):
        pass

class SensorPeso(Sensor):
    areaDeteccion = models.CharField(max_length=50)
    
    def medirPeso(self):
        pass

class SensorGPS(Sensor):
    def obtenerUbicacion(self):
        pass

class SensorProximidad(Sensor):
    frecuencia = models.DecimalField(max_digits=5, decimal_places=2)

    def medirDistancia(self):
        pass