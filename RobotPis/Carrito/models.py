from django.db import models

class ControladorMotor(models.Model):
    imagen = models.URLField(max_length=200, null=True,blank=True)
    estado = models.BooleanField(default=False)
    VOLTAJE = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    nombre = models.CharField(max_length=50, default="Controlador de Motor")

    def cambiar_estado(self, nuevo_estado):
        pass
    
    def forward(self):
        pass

    def reverse(self):
        pass

    def rotate(self):
        pass

    def brake(self):
        pass

    def __str__(self):
        return self.nombre

class MotorDC(models.Model):
    imagen = models.URLField(max_length=200, null=True,blank=True)
    VOLTAJE = models.DecimalField(max_digits=5, decimal_places=2)
    CORRIENTE = models.DecimalField(max_digits=5, decimal_places=2)
    nombre = models.CharField(max_length=50, default="Motor DC")
    maxVelocidad = models.DecimalField(max_digits=5, decimal_places=2)
    rpm = models.DecimalField(max_digits=5, decimal_places=2)
    torque = models.DecimalField(max_digits=5, decimal_places=2)
    controladorMotor = models.ForeignKey(ControladorMotor, on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.nombre