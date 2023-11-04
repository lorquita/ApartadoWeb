from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
import requests
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
@login_required
def inicio(request):
    if request.method == 'POST':
        username = request.POST['fre.camposo@duocuc.cl']
        password = request.POST['JuanitoPerez']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'core/inicio-sesion.html', {'error': 'Credenciales incorrectas. Inténtelo de nuevo.'})
    else:
        return render(request,'core/inicio-sesion.html')

@login_required
def home(request):
    cursos=Clase.objects.all()
    datos={'curso':cursos}

    response = requests.get('http://localhost:3000/clases')
    datos_json = response.json()

    return render(request, 'core/home.html', datos)

@login_required
def PagQR(request):
    return render(request, 'core/GenerarQR.html')

@login_required
def asistencia(request):
    alumno=Alumno.objects.all()
    datos={'alumno':alumno}

    response = requests.get('http://localhost:3000/alumnos')
    datos_json = response.json()

    return render(request, 'core/asistencia.html',datos)

@login_required
def login(request):
    return render(request,'core/registration/login.html')