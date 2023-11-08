from django.shortcuts import render
from .models import *
import requests

# Create your views here.

def inicio(request):
    return render(request, 'core/inicio-sesion.html')


def home(request):
    asignaturas=Asignauras.objects.all()
    datos={'asignaturas':asignaturas}

    response = requests.get('http://localhost:3000/asignaturas')
    datos_json = response.json()
    datos['datos_json'] = datos_json

    return render(request, 'core/home.html', datos)


def clase1(request):
    return render(request, 'core/Clase1.html')


def asistencia(request):
    alumno=AlumnoPM.objects.all()
    datos={'alumno':alumno}

    response = requests.get('http://localhost:3000/alumnos-PM')
    datos_json = response.json()

    datos['datos_json'] = datos_json

    return render(request, 'core/asistencia.html',datos)


def clase2(request):
    return render(request, 'core/Clase2.html')


def asist2(request):
    alumno=AlumnoBD.objects.all()
    datos={'alumno':alumno}

    response = requests.get('http://localhost:3000/alumnos-BD')
    datos_json = response.json()

    datos['datos_json'] = datos_json

    return render(request, 'core/asistencia2.html', datos)