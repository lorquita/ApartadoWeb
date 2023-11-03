from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio-sesion'),
    path('home', home, name='home'),
    path('asistencia', asistencia, name="asistencia"),
    path('PagQR',PagQR,name='PagQR'),
]
