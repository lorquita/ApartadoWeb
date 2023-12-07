from django.shortcuts import render, redirect
from .models import *
import requests
import qrcode
import qrcode.image.svg
from io import BytesIO
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login,logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password


# Create your views here.
#S@login_required
def home(request):
    asignaturas=Asignauras.objects.all()
    datos={'asignaturas':asignaturas}

    response = requests.get('http://localhost:3000/asignaturas')
    datos_json = response.json()
    datos['datos_json'] = datos_json

    return render(request, 'core/home.html', datos)

#@login_required
def clase1(request):
    context = {}

    url = 'http://localhost:3000/asignaturas'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  

        data_list = response.json()
        if isinstance(data_list, list) and data_list:
            data = data_list[0]

            factory = qrcode.image.svg.SvgImage
            qr_text = f"{data['nombre']} - {data['seccion']} - Sala: {data['sala']} - Hora: {data['hora inicio']} - {data['hora termino']}"
            img = qrcode.make(qr_text, image_factory=factory, box_size=20)
            stream = BytesIO()
            img.save(stream)
            context["svg"] = stream.getvalue().decode().replace("svg:rect", "rect")
            context["data"] = data
        else:
            context["error_message"] = "La respuesta del servidor JSON no es una lista válida o está vacía."
    except requests.RequestException as e:
        print(f"Error en la solicitud: {e}")
        context["error_message"] = "Error en la solicitud al servidor JSON."

    return render(request, 'core/Clase1.html', context=context)

#@login_required
def clase2(request):
    context = {}

    url = 'http://localhost:3000/asignaturas/2' 
    try:
            response = requests.get(url)
            response.raise_for_status()  

            data = response.json()

            factory = qrcode.image.svg.SvgImage
            qr_text = f"{data['nombre']} - {data['seccion']} - Sala: {data['sala']} - Hora: {data['hora inicio']} - {data['hora termino']}"
            img = qrcode.make(qr_text, image_factory=factory, box_size=20)
            stream = BytesIO()
            img.save(stream)
            context["svg"] = stream.getvalue().decode().replace("svg:rect", "rect")
            context["data"] = data
    except requests.RequestException as e:
            print(f"Error en la solicitud: {e}")
            context["error_message"] = "Error en la solicitud al servidor JSON."
    return render(request, 'core/Clase2.html', context=context)

#@login_required
def asistencia(request):
    alumno=AlumnoPM.objects.all()
    datos={'alumno':alumno}

    response = requests.get('http://localhost:3000/alumnos-PM')
    datos_json = response.json()

    datos['datos_json'] = datos_json

    return render(request, 'core/asistencia.html',datos)

#@login_required
def asist2(request):
    alumno=AlumnoBD.objects.all()
    datos={'alumno':alumno}

    response = requests.get('http://localhost:3000/alumnos-BD')
    datos_json = response.json()

    datos['datos_json'] = datos_json

    return render(request, 'core/asistencia2.html', datos)

@csrf_exempt
def inicio(request, *args, **kwargs):
    print(request.method)
    if request.method == 'POST':
        correo = request.POST.get('Email')
        contraseña = request.POST.get('password')
        url = 'http://localhost:3000/profesores'
        response = requests.get(url, params={'correo': correo})
        
        if response.status_code == 200:
            profesores = response.json()

            for profesor in profesores:
                profesor_rut = profesor.get('rut')
                profesor_correo=profesor.get('correo')
                profesor_contraseña = profesor.get('contraseña')
                print(profesor_correo)
                print(profesor_contraseña)
                print("-----------------")
                print(correo)
                print(contraseña)
                if correo == profesor_correo and contraseña == profesor_contraseña:
                    #user = authenticate(request, username=profesor_correo, password=contraseña)
                        return redirect('home')
            
            return JsonResponse({'success': False, 'error': 'Usuario no encontrado'})
        else:
            return JsonResponse({'success': False, 'error': 'Error al comunicarse con el servidor JSON'})

    return render(request, 'core/inicio.html')

def salir(request):
    logout(request)
    return redirect('/')