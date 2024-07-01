import requests
from django.shortcuts import render, redirect
from Carrito.models import *
from Sensores.views import *
from .models import *
from django.http import HttpResponse
# Create your views here.

def materiales(request):
    return render(request, 'materiales.html')

def desarrolladores(request):
    return render(request, 'desarrolladores.html')

def documentacion(request):
    return render(request, 'documentacion.html')

def funcionamiento (request):
    return render(request, 'funcionamiento.html')

def testimonios(request):
    if request.method == 'POST':
        form = TestimonioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimonios') 
    else:
        form = TestimonioForm()

    testimonios = Testimonio.objects.all().order_by('fecha')
    content = {
        'form': form, 
        'testimonios': testimonios
        }
    return render(request, 'testimonios.html', content)

def diagramaClases (request):
    return render(request, 'diagramaClases.html')

def materias (request):
    return render(request, 'materias.html')

def historiaUsuario(request):
    return render(request, 'historiasUsuario.html')

def control_servo(request):
    if 'camera' in request.GET and 'base' in request.GET:
        camera = request.GET['camera']
        base = request.GET['base']
        esp32_ip = 'http://10.20.136.210' # Cambia a la IP de tu ESP32
        response = requests.get(f'{esp32_ip}/?camera={camera}&base={base}')
        return HttpResponse(f'Servomotores movidos a {camera} y {base} grados', content_type='text/plain')
    
    return render(request, 'control.html')