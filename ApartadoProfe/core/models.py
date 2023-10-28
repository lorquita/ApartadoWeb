from django.db import models

# Create your models here.
class Seccion(models.Model):
    idSeccion=models.IntegerField(primary_key=True)
    Seccion=models.CharField(max_length=20)

    def __str__(self):
        return self.Seccion

class Sala(models.Model):
    idSala=models.IntegerField(primary_key=True)
    Sala=models.CharField(max_length=4)

    def __str__(self):
        return self.Sala

class Curso(models.Model):
    idCurso=models.IntegerField(primary_key=True) 
    nombreCurso=models.CharField(max_length=60)
    Seccion=models.ForeignKey(Seccion, on_delete=models.CASCADE)
    Sala=models.ForeignKey(Sala, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreCurso


class Carrera(models.Model):
    idCarrera=models.IntegerField(primary_key=True)
    nombreCarrera=models.CharField(max_length=100)

    def __str__(self):
        return self.nombreCarrera

class Alumno(models.Model):
    rutAlumno=models.CharField(primary_key=True, max_length=9)
    nombreAlumno=models.CharField(max_length=100)
    nombreCarrera=models.ForeignKey(Carrera, on_delete=models.CASCADE)

    def __str__(self):
        return self.rutAlumno

class Profesor(models.Model):
    rutProfesor=models.CharField(primary_key=True, max_length=9)
    nombreProfesor=models.CharField(max_length=100)

    def __str__(self):
        return self.rutProfesor

