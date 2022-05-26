from .models import Discografica, Grupo_Musical
from rest_framework import serializers

class DiscograficaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Discografica
    # fields = ['id', 'titulo', 'imagen', 'estreno', 'resumen']
    fields = '__all__'

class GruposSerializer(serializers.ModelSerializer):
  class Meta:
    model = Grupo_Musical
    # fields = ['id', 'titulo', 'imagen', 'estreno', 'resumen']
    fields = '__all__'