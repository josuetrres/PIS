from django.shortcuts import render
import requests
from django.http import HttpResponse

# Create your views here.
def control(request):
    if ('base' in request.GET and 'hombro' in request.GET and 'muneca' in request.GET and 'codo' in request.GET and 'pinza' in request.GET and 'camera' in request.GET and 'forward' in request.GET and 'backward' in request.GET and 'left' in request.GET and 'right' in request.GET) :
        camera = request.GET['camera']
        base = request.GET['base']
        hombro = request.GET['hombro']
        codo = request.GET['codo']
        muneca = request.GET['muneca']
        pinza = request.GET['pinza']
        forward = request.GET['forward']
        backward = request.GET['backward']
        left = request.GET['left']
        right = request.GET['right']

        esp32_ip = 'http://192.168.100.61' # Cambia a la IP de tu ESP32
        response = requests.get(f'{esp32_ip}/?base={base}&hombro={hombro}&codo={codo}&muneca={muneca}&pinza={pinza}&camera={camera}&forward={forward}&backward={backward}&left={left}&right={right}')

        return HttpResponse(f'Servomotores movidos', content_type='text/plain')
    
    return render(request, 'control.html')

def estadisticas(request):
    return render(request, 'estadisticas.html')