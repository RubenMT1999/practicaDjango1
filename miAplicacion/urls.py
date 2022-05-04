from django.urls import path
from miAplicacion.views import *

urlpatterns = [
    path('inicio/', inicioView),
    path('albums/',albumsView,name='albums'),
    path('grupos/',gruposView,name='grupos'),
    path('crear/',crearView,name='crear'),
    path('artistas/',artistasView,name='artistas'),
    path('crearAlbum/',crearAlbumView,name='crearAlbum'),
    path('crearGrupo/',crearGrupoView,name='crearGrupo'),
    path('crearArtista/',crearArtistaView,name='crearArtista'),
    path('borrarAlbum/<int:id>/',borrarAlbumView,name='borrarAlbum'),
    path('borrarGrupo/<int:id>/',borrarGrupoView,name='borrarGrupo'),
    path('borrarArtista/<int:id>/',borrarArtistaView,name='borrarArtista'),
    path('editarAlbum/<int:id>/',editarAlbumView,name='editarAlbum'),
    path('editarGrupo/<int:id>/',editarGrupoView,name='editarGrupo'),
    path('editarArtista/<int:id>/',editarArtistaView,name='editarArtista'),
]
