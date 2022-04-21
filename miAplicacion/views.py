from django.http import HttpResponse
from django.shortcuts import render
from miAplicacion.models import *

# Create your views here.
def inicioView(request):
    return render(request,"inicio.html")

def albumsView(request):
    allAlbums = Album.objects.all()
    context = {'allAlbums': allAlbums}
    return render(request,"albums.html",context)

def gruposView(request):
    allgrupos = Grupo_Musical.objects.all()
    context = {'allgrupos': allgrupos}
    return render(request,"grupos.html",context)

def crearView(request):
    return render(request,"crear.html")