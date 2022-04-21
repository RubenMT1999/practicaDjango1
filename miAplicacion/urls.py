from django.urls import path
from miAplicacion.views import *

urlpatterns = [
    path('inicio/', inicioView),
    path('albums/',albumsView,name='albums'),
    path('grupos/',gruposView,name='grupos'),
]
