from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from .models import Familiar

# Create your views here.

def agregar_familiar(request, nombre, apellido, edad, nacimiento):

    familiar = Familiar(nombre = nombre, apellido = apellido, edad = edad, nacimiento = nacimiento)
    familiar.save()

    return HttpResponse (f"<p>{familiar.nombre} ha sido añadid@ con exito!</p>")

def lista_familiares(request):

    lista = Familiar.objects.all()

    return render(request, "lista_familiares.html", {"lista_familiares": lista})