from django.urls import path
from .views import *

urlpatterns = [
    path('datos/', DatosView, name='datos'),
]