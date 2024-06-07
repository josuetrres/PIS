from django.shortcuts import render
from .models import *

# Create your views here.
def sensor(request):
    sensorTemp = SensorTemperatura.objects.all()
    sensorPeso = SensorPeso.objects.all()
    sensorGPS = SensorGPS.objects.all()
    sensorProx = SensorProximidad.objects.all()
    sensores = [sensorTemp, sensorPeso, sensorGPS, sensorProx]
    content = {
        'sensoresTotales': sensores,
    }
    return render(request, 'sensores.html', content)

def sensorDetail(request, id):
    sensor = Sensor.objects.get(id=id)
    content = {
        'sensor': sensor
    }
    return render(request, 'sensorDetail.html', content)
