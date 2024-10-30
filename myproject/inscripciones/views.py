from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import forms

# Create your views here.
@login_required(login_url="/users/login/")
def nueva_inscripcion(request):
    if request.method == 'POST':
         form = forms.CreateInscripcion(request.POST)
         if form.is_valid():
              form.save()
              messages.success(request, "Tu subscripcion se procesó correctamente")
              return redirect("home")
    else:
        form = forms.CreateInscripcion()
    return render(request, 'inscripciones/nueva_inscripcion.html', {'form': form})
