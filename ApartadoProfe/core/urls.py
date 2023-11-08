from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio-sesion'),
    path('accounts/login/', inicio, name='login'),
    path('home', home, name='home'),
    path('asistencia', asistencia, name="asistencia"),
    path('clase1',clase1,name='clase1'),
    path('clase2',clase2,name='clase2'),
    path('asist2',asist2,name='asist2'),
    path('accounts/login/home', home, name='home'),
    path('accounts/login/home', asistencia, name='asistencia'),
    path('accounts/login/home', clase1, name='clase1'),
    path('accounts/login/home', clase2, name='clase2'),
    path('accounts/login/home', asist2, name='asist2'),
]
