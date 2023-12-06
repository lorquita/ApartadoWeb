from django.db import models

class AlumnoPM(models.Model):
    rut = models.CharField(primary_key=True, max_length=12, unique=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    carrera = models.CharField(max_length=200)
    asistencia = models.IntegerField()

class AlumnoBD(models.Model):
    rut = models.CharField(primary_key=True, max_length=12, unique=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    carrera = models.CharField(max_length=200)
    porcentaje = models.IntegerField()

class Asignauras(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=200)
    seccion = models.CharField(max_length=10)
    sala = models.CharField(max_length=6)

class Profesor(models.Model):
    rut=models.CharField(primary_key=True, max_length=12, unique=True)
    nombre=models.CharField(max_length=200)
    titulo=models.CharField(max_length=200)