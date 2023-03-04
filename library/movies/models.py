from django.db import models
from uuid import uuid4
'''
class Users(models.Model):
    idUser = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)
'''

class Movies(models.Model):

    idMovie = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    diretor = models.CharField(max_length=255)
    ano = models.IntegerField()


class Rating(models.Model):

    id = models.AutoField(primary_key=True)
    idMovie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=3, decimal_places=1, default= 0)


