from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    return render(request, 'home.html')

def servo(request):
    servos = Servo.objects.all()
    return render(request, 'servo.html', {'servos': servos})


def articulacion(request):
    bases = Base.objects.all()
    codos = Codo.objects.all()
    hombros = Hombro.objects.all()
    munecas = Muneca.objects.all()
    pinzas = Pinza.objects.all()
    return render(request, 'articulacion.html', {
        'bases': bases,
        'codos': codos,
        'hombros': hombros,
        'munecas': munecas,
        'pinzas' : pinzas,
        })

def servodetail(request, id):
    servo = Servo.objects.get(id=id)
    context = {
        'servo': servo
    }
    return render(request, 'servodetail.html', context)

