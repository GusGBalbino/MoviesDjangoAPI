from rest_framework import serializers
from moviesAPIs import models

class DiretorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Diretor
        fields = '__all__'

class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Filme
        fields = '__all__'

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Avaliacao
        fields = '__all__'