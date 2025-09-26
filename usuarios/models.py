from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    rol = models.CharField(max_length=50, choices=[('estudiante', 'Estudiante'), ('instructor', 'Instructor')]) 

    def __str__(self):
        return self.nombre