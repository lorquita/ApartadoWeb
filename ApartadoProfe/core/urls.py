from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio-sesion'),
    path('home', home, name='home'),
    path('asistencia', asistencia, name="asistencia"),
    path('QR/',QR,name='QR'),
    path('api/generate-qr/<str:data>/', generate_qr_code, name='generate_qr_code'),
]
