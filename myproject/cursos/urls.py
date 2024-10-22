from django.urls import path
from . import views

app_name = 'cursos'

urlpatterns = [
    path('', views.cursos_list, name="list"),
    path('<slug:slug>', views.curso_page, name="page"),
    
]