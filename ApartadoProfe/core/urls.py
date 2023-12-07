from django.urls import path
from .views import *

urlpatterns = [
    path('home', home, name='home'),
    path('asistencia', asistencia, name="asistencia"),
    path('clase1',clase1,name='clase1'),
    path('asist2',asist2,name='asist2'),
    path('',inicio,name='inicio'),
    path('salir/',salir,name='salir'),
    path('clase2',clase2,name='clase2')
]
