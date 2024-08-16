from django.db import models

# Create your models here.

class Persona(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    fono = models.IntegerField()

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"