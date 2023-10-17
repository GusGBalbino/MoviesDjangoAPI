from rest_framework import viewsets
from moviesAPIs.api import serializers
from moviesAPIs import models
from rest_framework.decorators import action
from rest_framework.response import Response

class DiretorViewSet(viewsets.ModelViewSet):
    queryset = models.Diretor.objects.all()
    serializer_class = serializers.DiretorSerializer
    

class FilmeViewSet(viewsets.ModelViewSet):
    queryset = models.Filme.objects.all()
    serializer_class = serializers.FilmeSerializer
    
    @action(detail=True, methods=['get'])
    def media_notas(self, request, pk=None):
        filme = self.get_object()
        media = models.Avaliacao.objects.filter(filme=filme).aggregate(models.Avg('nota'))
        return Response({'Média': media['nota__avg']})
    
    def get_queryset(self):
        diretor_id = self.request.query_params.get('diretor', None)
        if diretor_id:
            return models.Filme.objects.filter(diretor_id=diretor_id)
        return models.Filme.objects.all()
         
class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = models.Avaliacao.objects.all()
    serializer_class = serializers.AvaliacaoSerializer
    

