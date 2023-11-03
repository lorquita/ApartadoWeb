from django.db import models

class Alumno(models.Model):
    rut = models.CharField(primary_key=True, max_length=12, unique=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    carrera = models.CharField(max_length=200)
    porcentaje = models.IntegerField()

class Clase(models.Model):
    id = models.IntegerField(primary_key=True)
    asignatura = models.CharField(max_length=200)
    seccion = models.CharField(max_length=10)
    sala = models.CharField(max_length=6)
