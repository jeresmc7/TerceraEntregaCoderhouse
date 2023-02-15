from django.db import models

# Create your models here.

class Juego(models.Model):
    nombre = models.CharField(max_length=40)
    categoria = models.CharField(max_length=40)
    valoracion = models.IntegerField()

    def __str__(self) -> str:
        return self.nombre + ' (' + str(self.valoracion) + ')'

class Categoria(models.Model):
    nombre = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.nombre

class Lanzamiento(models.Model):
    nombre = models.CharField(max_length=40)
    categoria = models.CharField(max_length=40)
    fecha_de_lanzamiento = models.DateField()

    def __str__(self) -> str:
        return self.nombre + ' (' + str(self.fecha_de_lanzamiento) + ')'
    
    
    # class Meta:
    #     verbose_name_plural = 'Lanzamientos'
