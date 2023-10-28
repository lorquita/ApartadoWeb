from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
import qrcode
from io import BytesIO
from django.http import JsonResponse
import base64
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
#Aqui va el @login_required
def inicio(request):
    return render(request,'core/inicio-sesion.html')

#Aqui va el @login_required
def home(request):
    cursos=Curso.objects.all()
    datos={'curso':cursos}
    return render(request, 'core/home.html', datos)

def QR(request):
    return render(request, 'QR.html')
#Aqui va el @login_required
def generate_qr_code(request, data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    return JsonResponse({'qr_code': img_str})

#Aqui va el @login_required
def asistencia(request):
    alumno=Alumno.objects.all()
    datos={'alumno':alumno}
    return render(request, 'core/asistencia.html',datos)

def qr_data(request):
    if request.method == 'POST':
        recived_data = request.POST.get('data')