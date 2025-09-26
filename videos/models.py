from django.db import models

# Create your models here.
class Video(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    url_video = models.URLField() 
    fecha_subida = models.DateTimeField(auto_now_add=True)
    duracion = models.DurationField(blank=True, null=True)  

    def __str__(self):
        return self.titulo