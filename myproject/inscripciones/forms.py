from django import forms
from . import models


class CreateInscripcion(forms.ModelForm):
    class Meta:
        model = models.Inscripcion
        fields = ['username', 'first_name', 'last_name', 'email', 'curso_inscripcion']