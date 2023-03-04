from rest_framework import serializers
from movies import models

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movies
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rating
        fields = '__all__'