from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    disponibilidad = models.BooleanField()
    cantidad = models.IntegerField()
    categoria = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

