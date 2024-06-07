"""
URL configuration for RobotPis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from BrazoRobotico.views import home, servo, articulacion, servodetail
from Carrito.views import controladorMotor, motorDC
<<<<<<< HEAD
from WebSite.views import *
=======
from WebSite.views import materiales, desarrolladores
>>>>>>> 8db5d00427aca1037420bd37e002e3a71b0414eb

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'), 
    path('servo/',servo, name='servo'),
    path('servo/<int:id>/', servodetail, name='servodetail'),
    path('articulaciones/', articulacion, name='articulaciones'),
    path('controladorMotor/', controladorMotor, name='controladorMotor'),
    path('motorDC/', motorDC, name='motorDC'),
    path('materiales/', materiales, name='materiales'),
<<<<<<< HEAD
    path('testimonios/', testimonios, name='testimonios'),
=======
>>>>>>> 8db5d00427aca1037420bd37e002e3a71b0414eb
    path('desarrolladores/', desarrolladores, name='desarrolladores'),
]
