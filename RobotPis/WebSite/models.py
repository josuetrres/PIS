from django.db import models
from django import forms

# Create your models here.
class Testimonio(models.Model):
    nombre = models.CharField(max_length=100)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + '-' + self.mensaje
    
class TestimonioForm(forms.ModelForm):
    class Meta:
        model = Testimonio
        fields = ['nombre', 'mensaje']
    