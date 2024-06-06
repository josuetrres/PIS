from django.db import models

class ControladorMotor(models.Model):
    estado = models.BooleanField()


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


class MotorDC(models.Model):
    ontroladorMotor = models.ForeignKey(ControladorMotor, on_delete = models.DO_NOTHING)
    VOLTAJE = models.DecimalField(max_digits=5,  decimal_places=2)
    CORRIENTE = models.DecimalField(max_digits=5,  decimal_places=2)
    maxVelocidad = models.DecimalField(max_digits=5, decimal_places=2)
    rpm = models.DecimalField(max_digits=5, decimal_places=2)
    torque = models.DecimalField(max_digits=5, decimal_places=2)