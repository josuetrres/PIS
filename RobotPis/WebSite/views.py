from django.shortcuts import render
from Carrito.models import *
from Testimonios.views import *
# Create your views here.

def materiales(request):
    return render(request, 'materiales.html')

<<<<<<< HEAD
def desarrolladores(request):
    return render(request, 'desarrolladores.html')
=======
def desarrolladores (request):
    return render(request, 'desarrolladores.html')
>>>>>>> 8db5d00427aca1037420bd37e002e3a71b0414eb
