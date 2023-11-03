from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
import requests


# Create your views here.

def inicio(request):
    return render(request,'core/inicio-sesion.html')


def home(request):
    cursos=Clase.objects.all()
    datos={'curso':cursos}

    response = requests.get('http://localhost:3000/clases')
    datos_json = response.json()

    #for clase in datos_json['clase']:
        #Clase.objects.create(id=clase['Id'], asignatura=clase['asignatura'], seccion=clase['seccion'], sala=clase['sala'])
    return render(request, 'core/home.html', datos)

def PagQR(request):
    return render(request, 'core/GenerarQR.html')

def asistencia(request):
    alumno=Alumno.objects.all()
    datos={'alumno':alumno}

    response = requests.get('http://localhost:3000/alumnos')
    datos_json = response.json()

    #for alumno in datos_json['alumnos']:
        #Alumno.objects.create(rut=alumno['rut'], nombre=alumno['nombre'], apellido=alumno['apellido'], carrera=alumno['carrera'], porcentaje=alumno['porcentaje'])

    return render(request, 'core/asistencia.html',datos)
