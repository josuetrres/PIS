from django.shortcuts import render
from Carrito.models import *
from Testimonios.views import *
# Create your views here.

def materiales(request):
    return render(request, 'materiales.html')

def desarrolladores(request):
    return render(request, 'desarrolladores.html')

def vip(request):
    return render(request, 'vip.html')
