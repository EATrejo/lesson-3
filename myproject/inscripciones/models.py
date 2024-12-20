from django.db import models

# Create your models here.

class Inscripcion(models.Model):
    username = models.CharField(max_length=100, default='False')
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    curso_inscripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name
    

