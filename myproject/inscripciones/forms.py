from django import forms
from . import models


class CreateInscripcion(forms.ModelForm):
    class Meta:
        model = models.Inscripcion
        fields = ['first_name', 'last_name', 'email', 'alumno_inscripcion']