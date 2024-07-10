from django.shortcuts import render
import requests
from django.http import HttpResponse

# Create your views here.
def control(request):
    if 'camera' in request.GET and 'base' in request.GET:
        camera = request.GET['camera']
        base = request.GET['base']
        esp32_ip = 'http://192.168.100.61' # Cambia a la IP de tu ESP32
        response = requests.get(f'{esp32_ip}/?camera={camera}&base={base}')
        return HttpResponse(f'Servomotores movidos a {camera} y {base} grados', content_type='text/plain')
    
    return render(request, 'control.html')

def estadisticas(request):
    return render(request, 'estadisticas.html')