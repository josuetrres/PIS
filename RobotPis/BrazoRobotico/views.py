from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    return render(request, 'home.html')

def servo(request):
    servos = Servo.objects.all()
    return render(request, 'servo.html', {'servos': servos})

def articulacion(request):
    articulaciones = Articulacion.objects.all()
    return render(request, 'articulacion.html', {'articulaciones': articulaciones})

def base(request):
    base = Base.objects.all()
    return render(request, 'base.html', {'base': base})

