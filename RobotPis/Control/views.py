from django.shortcuts import render

# Create your views here.
# views.py
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def video_upload(request):
    if request.method == 'POST':
        video_file = request.body
        # Procesar y guardar el video en el servidor
        return HttpResponse('Video recibido correctamente', status=200)
    else:
        return HttpResponse('Método no permitido', status=405)