from .models import Discografica
from rest_framework import serializers

class DiscograficaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Discografica
    # fields = ['id', 'titulo', 'imagen', 'estreno', 'resumen']
    fields = '__all__'