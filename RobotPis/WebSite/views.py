from django.shortcuts import render
from Carrito.models import *
# Create your views here.

def materiales(request):
    return render(request, 'materiales.html')