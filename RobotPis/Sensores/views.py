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
    sensorTemp = SensorTemperatura.objects.all()
    sensorPeso = SensorPeso.objects.all()
    sensorGPS = SensorGPS.objects.all()
    sensorProx = SensorProximidad.objects.all()
    sensores_list = [sensorTemp, sensorPeso, sensorGPS, sensorProx]

    for sensores in sensores_list:
        for sensor in sensores:
            if sensor.id == id:
                if type(sensor) == SensorTemperatura:
                    sensor = SensorTemperatura.objects.get(id=id)
                elif type(sensor) == SensorPeso:
                    sensor = SensorPeso.objects.get(id=id)
                elif type(sensor) == SensorGPS:
                    sensor = SensorGPS.objects.get(id=id)
                elif type(sensor) == SensorProximidad:
                    sensor = SensorProximidad.objects.get(id=id)

    content = {
        'sensor': sensor
    }
    return render(request, 'sensorDetail.html', content)
