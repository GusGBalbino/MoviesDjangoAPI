from django.urls import path, include
from rest_framework.routers import DefaultRouter
from moviesAPIs.api import viewsets
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register(r'diretores', viewsets.DiretorViewSet)
router.register(r'filmes', viewsets.FilmeViewSet)
router.register(r'avaliacoes', viewsets.AvaliacaoViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Movies APIs",
      default_version='v1.0',
      description="APIs refeitas e muito melhores.",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]