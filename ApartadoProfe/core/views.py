from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
import qrcode
from io import BytesIO
from django.http import JsonResponse
import base64
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def inicio(request):
    return render(request,'core/inicio-sesion.html')


def home(request):
    cursos=Curso.objects.all()
    datos={'curso':cursos}
    return render(request, 'core/home.html', datos)

def PagQR(request):
    return render(request, 'core/GenerarQR.html')

def asistencia(request):
    alumno=Alumno.objects.all()
    datos={'alumno':alumno}
    return render(request, 'core/asistencia.html',datos)

def qr_data(request):
    if request.method == 'POST':
        recived_data = request.POST.get('data')