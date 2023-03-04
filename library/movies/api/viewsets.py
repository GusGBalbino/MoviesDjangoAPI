from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from movies.api import serializers
from movies import models
from movies.models import Rating


#class MovieViewSet(viewsets.ModelViewSet):
    #serializer_class = serializers.MovieSerializer
    #queryset = models.Movies.objects.all()

class MoviesList(viewsets.ModelViewSet):
    queryset = models.Movies.objects.all()
    serializer_class = serializers.MoviesSerializer

class RatingList(viewsets.ModelViewSet):
    queryset = models.Rating.objects.all()
    serializer_class = serializers.RatingSerializer

class TotalRating(viewsets.ModelViewSet):

    serializer_class = serializers.RatingSerializer

    def list(self, request, id_movie=None):
        
        filter_movies = models.Rating.objects.filter(idMovie = id_movie)

        qtd = len(filter_movies)

        totalNotas = 0

        for movie in filter_movies:
            totalNotas += int(movie.nota)

        total = totalNotas/qtd if qtd > 0 else 0

        return Response({'Total': total})
