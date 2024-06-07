from django.db import models

# Create your models here.
class Servo(models.Model):
    imagen = models.URLField(max_length=200, null=True,blank=True)
    VOLTAJE = models.DecimalField(max_digits=5, decimal_places=2)
    CORRIENTE = models.DecimalField(max_digits=5, decimal_places=2)
    nombre = models.CharField(max_length=50)
    torque = models.DecimalField(max_digits=5, decimal_places=2)
    velocidad = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nombre
    
class Articulacion(models.Model):
    imagen = models.URLField(max_length=200, null=True,blank=True)
    nombre = models.CharField(max_length=50)
    angulo = models.DecimalField(max_digits=5, decimal_places=2)
    velocidad = models.DecimalField(max_digits=5, decimal_places=2)
    servo = models.ForeignKey(Servo, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def definirPosicionInicial(self):
        pass

    def __str__(self):
        return self.nombre

class Base(Articulacion):
    def definirPosicionInicial(self):
        self.angulo = 0
    
    def rotar(self, angulo):
        self.angulo = angulo

class Hombro(Articulacion):
    def definirPosicionInicial(self):
        self.angulo = 0
    
    def ascender(self):
        pass

    def descender(self):
        pass

class Codo(Articulacion):
    def definirPosicionInicial(self):
        self.angulo = 0
    
    def flexionar(self):
        pass

    def extender(self):
        pass

class Muneca(Articulacion):
    def definirPosicionInicial(self):
        self.angulo = 0
    
    def doblar(self):
        pass

class Pinza(Articulacion):
    def definirPosicionInicial(self):
        self.angulo = 0
    
    def cerrar(self):
        pass

    def abrir(self):
        pass