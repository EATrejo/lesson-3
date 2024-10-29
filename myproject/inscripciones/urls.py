from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'inscripciones'

urlpatterns = [
    #path('', views.nueva_inscripcion),
    path('nueva-inscripcion', views.nueva_inscripcion, name='nueva-inscripcion'),
    
]