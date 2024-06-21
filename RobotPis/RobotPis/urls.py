from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from BrazoRobotico.views import home, servo, articulacion, servodetail
from Carrito.views import controladorMotor, motorDC
from WebSite.views import *
from Control.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'), 
    path('servo/',servo, name='servo'),
    path('servo/<int:id>/', servodetail, name='servodetail'),
    path('articulaciones/', articulacion, name='articulaciones'),
    path('controladorMotor/', controladorMotor, name='controladorMotor'),
    path('motorDC/', motorDC, name='motorDC'),
    path('materiales/', materiales, name='materiales'),
    path('testimonios/', testimonios, name='testimonios'),
    path('desarrolladores/', desarrolladores, name='desarrolladores'),
    path('documentacion/', documentacion, name='documentacion'),
    path('funcionamiento/', funcionamiento, name='funcionamiento'),
    path('diagramaClases/', diagramaClases, name='diagramaClases'),
    path('sensores/', sensor, name='sensores'),
    path('sensores/<int:id>/', sensorDetail, name='sensorDetail'),
    path('materias/', materias, name='materias'),
    path('historiaUsuario/', historiaUsuario, name='historiaUsuario'),
    path('video-upload/', video_upload, name='video_upload'),
]

# Esta línea es la que debes agregar para servir archivos multimedia durante el desarrollo
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


