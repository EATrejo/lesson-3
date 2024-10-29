from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
@login_required(login_url="/users/login/")
def nueva_inscripcion(request):
    if request.method == 'POST':
         form = forms.CreateInscripcion(request.POST)
         if form.is_valid():
              form.save()
              return HttpResponse("<h1>Tu subscripcion se procesó correctamente.</h1>")
    else:
        form = forms.CreateInscripcion()
    return render(request, 'inscripciones/nueva_inscripcion.html', {'form': form})
