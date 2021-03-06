import requests
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from rest_framework import viewsets

from miAplicacion.models import *
import datetime

# Create your views here.
from miAplicacion.serializers import DiscograficaSerializer, GruposSerializer


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

def artistasView(request):
    allArtistas = Artista.objects.all()
    context = {'allArtistas': allArtistas}
    return render(request,"artistas.html",context)


def crearAlbumView(request):
    if request.method == 'GET':
        allGrupos = Grupo_Musical.objects.all()
        allArtistas = Artista.objects.all()
        return render(request, "crearAlbum.html", {'allGrupos': allGrupos, 'allArtistas':allArtistas})
    else:
        nuevoAlbum = Album()
        nuevoAlbum.nombreAlbum = request.POST['nombre']
        nuevoAlbum.anio = request.POST['anio']
        nuevoAlbum.genero = request.POST['genero']
        nuevoAlbum.grupoMusical_id = Grupo_Musical.objects.get(nombreGrupo=request.POST['grupo'])
        nuevoAlbum.artista_id = Artista.objects.get(nombre= request.POST['artista'])
        nuevoAlbum.puntuacion = request.POST['puntuacion']
        Album.save(nuevoAlbum)
        return redirect('/albums')

def crearGrupoView(request):
    if request.method == 'GET':
        return render(request, "crearGrupo.html")
    else:
        nuevoGrupo = Grupo_Musical()
        nuevoGrupo.nombreGrupo = request.POST['nombre']
        nuevoGrupo.estiloMusica = request.POST['estilo']
        nuevoGrupo.fecha_creacion = request.POST['fechaCreacion']
        miFecha = request.POST['FechaDisolucion']
        if miFecha is not "":
            nuevoGrupo.fecha_disolucion = datetime.datetime.strptime(miFecha, "%Y-%m-%d")
        else:
            nuevoGrupo.fecha_disolucion = None
        Grupo_Musical.save(nuevoGrupo)
        return redirect('/grupos')


def crearArtistaView(request):
    if request.method == 'GET':
        allGrupos = Grupo_Musical.objects.all()
        context = {'allGrupos':allGrupos}
        return render(request,'crearArtista.html',context)
    else:
        nuevoArtista = Artista()
        nuevoArtista.nombre = request.POST['nombre']
        nuevoArtista.apellido1 = request.POST['primerApellido']
        nuevoArtista.apellido2 = request.POST['segundoApellido']
        nuevoArtista.grupo_id = Grupo_Musical.objects.get(nombreGrupo=request.POST['grupo'])
        Artista.save(nuevoArtista)
        return redirect('/artistas')


def borrarAlbumView(request,id):
    albunBorrar = Album.objects.get(id= id)
    albunBorrar.delete()
    return redirect('/albums')

def borrarGrupoView(request,id):
    grupoBorrar = Grupo_Musical.objects.get(id= id)
    grupoBorrar.delete()
    return redirect('/grupos')

def borrarArtistaView(request,id):
    artistaBorrar = Artista.objects.get(id= id)
    artistaBorrar.delete()
    return redirect('/artistas')


def editarAlbumView(request,id):
    if request.method == 'GET':
        allAlbums = Album.objects.get(id = id)
        allGrupos  = Grupo_Musical.objects.all()
        allArtistas = Artista.objects.all()
        return render(request,'editarAlbum.html',{'allAlbums':allAlbums, 'allGrupos':allGrupos, 'allArtistas':allArtistas })
    else:
        obtenerAlbum = Album.objects.get(id = id)
        obtenerAlbum.nombreAlbum = request.POST['nombre']
        obtenerAlbum.anio = request.POST['anio']
        obtenerAlbum.genero = request.POST['genero']
        obtenerAlbum.grupoMusical_id = Grupo_Musical.objects.get(nombreGrupo= request.POST['grupo'])
        obtenerAlbum.artista_id = Artista.objects.get(nombre= request.POST['artista'])
        obtenerAlbum.puntuacion = request.POST['puntuacion']
        obtenerAlbum.save()
        return redirect('/albums')


def editarGrupoView(request,id):
    if request.method == 'GET':
        allGrupos = Grupo_Musical.objects.get(id = id)
        #fechaFormateada = allGrupos.fecha_creacion.strftime("%Y-%m-%d")
        return render(request,'editarGrupo.html',{'allGrupos':allGrupos})
    else:
        grupoEditar = Grupo_Musical.objects.get(id = id)
        grupoEditar.nombreGrupo = request.POST['nombre']
        grupoEditar.estiloMusica = request.POST['estilo']
        grupoEditar.fecha_creacion = request.POST.get('fechaCreacion')
        if request.POST.get('FechaDisolucion') is not "":
            grupoEditar.fecha_disolucion = request.POST.get('FechaDisolucion')
        else:
            grupoEditar.fecha_disolucion = None

        grupoEditar.save()
        return redirect('/grupos')


def editarArtistaView(request,id):
    if request.method == 'GET':
        allArtistas = Artista.objects.get(id = id)
        allGrupos = Grupo_Musical.objects.all()
        return render(request,'editarArtista.html',{'allArtistas':allArtistas,'allGrupos':allGrupos})
    else:
        artistaEditar = Artista.objects.get(id = id)
        artistaEditar.nombre = request.POST['nombre']
        artistaEditar.apellido1 = request.POST['primerApellido']
        artistaEditar.apellido2 = request.POST['segundoApellido']
        artistaEditar.grupo_id = Grupo_Musical.objects.get(nombreGrupo= request.POST['grupo'])
        artistaEditar.save()
        return redirect('/artistas')


def crearView(request):
    return render(request,"crear.html")





class DiscograficaViewSet(viewsets.ModelViewSet):
    queryset = Discografica.objects.all()
    serializer_class = DiscograficaSerializer

class GruposViewSet(viewsets.ModelViewSet):
    queryset = Grupo_Musical.objects.all()
    serializer_class = GruposSerializer
    #def grupo_redirect(request):
     #   return HttpResponseRedirect(redirect_to='https://google.com')




def pruebaView(request):
    url = "https://deezerdevs-deezer.p.rapidapi.com/artist/3"

    headers = {
        "X-RapidAPI-Host": "deezerdevs-deezer.p.rapidapi.com",
        "X-RapidAPI-Key": "49bd03d5fcmsh5a352edd72a9c9ap1a972djsnc8034406cdc5"
    }

    response = requests.request("GET", url, headers=headers)
    datos = response.json()
    nombre = datos.get('name')
    foto = datos.get('picture_big')
    numero_fans = datos.get('nb_fan')
    top_50 = datos.get('tracklist')

    return render(request,"prueba.html",{'nombre':nombre,'foto':foto,
                                         'numero_fans':numero_fans,'top_50':top_50})



def topHitsView(request,id):
    url = requests.get("https://api.deezer.com/artist/"+str(id)+"/top?limit=50").json()

    nombreHit = url.get('title')

    return render(request,"topHits.html",{'nombreHit':nombreHit})






