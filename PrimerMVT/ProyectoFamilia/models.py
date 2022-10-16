from django.db import models

# Create your models here.

class Familiar(models.Model):

    nombre = models.CharField(max_length=50)

    apellido = models.CharField(max_length=50)

    edad = models.IntegerField()

    nacimiento = models.DateField (auto_now=False, auto_now_add=False, null=True) #El formato en el que se agrega la fecha es YYYY-MM-DD


