from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Libro(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    autor = models.CharField(max_length=200)
    editorial = models.CharField(max_length=200)
    genero = models.CharField(max_length=200)
    cantidad = models.IntegerField(validators=[MinValueValidator(0)])


