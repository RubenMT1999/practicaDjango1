from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.

class Grupo_Musical(models.Model):
    nombreGrupo = models.CharField(max_length=50, blank=False)
    estiloMusica = models.CharField(max_length=50)
    fecha_creacion = models.DateField(blank=False)
    fecha_disolucion = models.DateField(null=True, blank=True, default=None)


class Artista(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    apellido1 = models.CharField(max_length=50, blank=False)
    apellido2 = models.CharField(max_length=50, blank=False)
    grupo_id = models.ForeignKey(Grupo_Musical, on_delete=models.CASCADE)


class Album(models.Model):
    nombreAlbum = models.CharField(max_length=50, blank=False)
    anio = models.IntegerField(default=0)
    genero = models.CharField(max_length=50, blank=False)
    artista_id = models.ForeignKey(Artista, on_delete=models.CASCADE, blank=True,null=True)
    grupoMusical_id = models.ForeignKey(Grupo_Musical, on_delete=models.CASCADE, blank=True,null=True)
    puntuacion = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])


class Cancion(models.Model):
    titulo = models.CharField(max_length=50, blank=False)
    duracion = models.TimeField(blank=False)
    generoCancion = models.CharField(max_length=50)
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True)
    artista_id = models.ForeignKey(Artista, on_delete=models.CASCADE, blank=False)



class Discografica(models.Model):
  nombre = models.CharField(max_length=150)
  fundacion = models.IntegerField(default=0)
  ingresos =  models.IntegerField(default=0)











