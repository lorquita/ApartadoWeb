from django.shortcuts import render
from .models import *
import requests
import qrcode
import qrcode.image.svg
from io import BytesIO
import json

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
    context={}
    
    if request.method =='POST':
        print(request.POST.get("qr_text"))
        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(request.POST.get("qr_text"), image_factory=factory, box_size=20)
        stream = BytesIO()
        img.save(stream)
        context["svg"] = stream.getvalue().decode().replace("svg:rect", "rect")
    return render(request, 'core/Clase1.html',context=context)


def asistencia(request):
    alumno=AlumnoPM.objects.all()
    datos={'alumno':alumno}

    response = requests.get('http://localhost:3000/alumnos-PM')
    datos_json = response.json()

    datos['datos_json'] = datos_json

    return render(request, 'core/asistencia.html',datos)

def asist2(request):
    alumno=AlumnoBD.objects.all()
    datos={'alumno':alumno}

    response = requests.get('http://localhost:3000/alumnos-BD')
    datos_json = response.json()

    datos['datos_json'] = datos_json

    return render(request, 'core/asistencia2.html', datos)