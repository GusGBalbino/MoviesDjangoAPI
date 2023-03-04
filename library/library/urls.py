from django.contrib import admin
from movies.api.viewsets import MoviesList, RatingList, TotalRating, NoRateList
from django.urls import path, include
from rest_framework import routers

route = routers.DefaultRouter()
route.register(r'movies', MoviesList, basename="Movies") #/movies

route_rating  = routers.DefaultRouter()
route_rating.register(r'rate', RatingList, basename="Rates") #/rate

route_total = routers.DefaultRouter()
route_total.register(r'total', TotalRating, basename="Total") #/total

route_norate = routers.DefaultRouter()
route_norate.register(r'norate', NoRateList, basename='NoRate' ) #/norate


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)), #movies
    path('', include(route_rating.urls)), #rate
    path('movies/<int:id_movie>/', include(route_total.urls)),
    path('', include(route_norate.urls)),#norate
]