from django.db import models
from django.contrib.auth.models import User

class Diretor(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
    
class Filme(models.Model):
    titulo = models.CharField(max_length=255)
    diretor = models.ForeignKey(Diretor, on_delete=models.CASCADE, related_name="filmes")
    ano_lancamento = models.PositiveIntegerField(null=True, blank=True)
    sinopse = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.titulo

class Avaliacao(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE, related_name="avaliacoes")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="avaliacoes")
    nota = models.PositiveIntegerField()
    comentario = models.TextField(null=True, blank=True)
    data_avaliacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Avaliação de {self.usuario.username} para {self.filme.titulo}: {self.nota}"