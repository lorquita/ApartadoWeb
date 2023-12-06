from django.shortcuts import render, redirect
from .models import *
import requests
import qrcode
import qrcode.image.svg
from io import BytesIO
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required
def home(request):
    asignaturas=Asignauras.objects.all()
    datos={'asignaturas':asignaturas}

    response = requests.get('http://localhost:3000/asignaturas')
    datos_json = response.json()
    datos['datos_json'] = datos_json

    return render(request, 'core/home.html', datos)

@login_required
def clase1(request):
    context={}

    if request.method =='POST':
        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(request.POST.get("qr_text"), image_factory=factory, box_size=20)
        stream = BytesIO()
        img.save(stream)
        context["svg"] = stream.getvalue().decode().replace("svg:rect", "rect")
    return render(request, 'core/Clase1.html',context=context)

@login_required
def asistencia(request):
    alumno=AlumnoPM.objects.all()
    datos={'alumno':alumno}

    response = requests.get('http://localhost:3000/alumnos-PM')
    datos_json = response.json()

    datos['datos_json'] = datos_json

    return render(request, 'core/asistencia.html',datos)

login_required
def asist2(request):
    alumno=AlumnoBD.objects.all()
    datos={'alumno':alumno}

    response = requests.get('http://localhost:3000/alumnos-BD')
    datos_json = response.json()

    datos['datos_json'] = datos_json

    return render(request, 'core/asistencia2.html', datos)

@csrf_exempt
def login(request, *args, **kwargs):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        contraseña = request.POST.get('contraseña')

        json_server_url = 'http://localhost:3000/profesores'
        response = requests.get(json_server_url, params={'correo': correo, 'contraseña': contraseña})

        if response.status_code == 200:
            user_data = response.json()
            user = authenticate(request, username=user_data['username'], password=contraseña)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return JsonResponse({'success': False, 'error': 'Credenciales inválidas'})
        else:
            return JsonResponse({'success': False, 'error': 'Error al comunicarse con el servidor JSON'})

    return render(request, 'core/login.html')

def salir(request):
    logout(request)
    return redirect('/')