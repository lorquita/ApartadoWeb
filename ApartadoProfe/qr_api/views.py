from django.shortcuts import render
import qrcode
from PIL import Image
import os
from django.http import JsonResponse
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def generardorQR(request, data):
    qr = qrcode.QRCode(
        version=1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4
    )

    qr.add_data("./confirmar-asistencia.page.html")
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("salida_qr.png")
    