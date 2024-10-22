from django.db import models

# Create your models here.

class Curso(models.Model):
    title = models.CharField(max_length=100)
    banner = models.ImageField(default='fallback.png', blank=True)
    description = models.TextField()
    duracion_curso = models.DurationField(null=True)
    lugar_curso = models.TextField()
    fecha_de_inicio = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
    costo_del_curso = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.title