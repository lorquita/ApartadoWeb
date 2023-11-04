# Generated by Django 4.2.1 on 2023-11-03 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('rut', models.CharField(max_length=12, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('carrera', models.CharField(max_length=200)),
                ('porcentaje', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('asignatura', models.CharField(max_length=200)),
                ('seccion', models.CharField(max_length=10)),
                ('sala', models.CharField(max_length=6)),
            ],
        ),
    ]
