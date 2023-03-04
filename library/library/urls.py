from django.contrib import admin
from movies.api.viewsets import MoviesList, RatingList, TotalRating
from django.urls import path, include
from rest_framework import routers

route = routers.DefaultRouter()

route.register(r'movies', MoviesList, basename="Movies")



route_rating  = routers.DefaultRouter()

route_rating.register(r'rate', RatingList, basename="Rates")


route_total = routers.DefaultRouter()

route_total.register(r'total', TotalRating, basename="Total")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path('', include(route_rating.urls)),
    path('movies/<int:id_movie>/', include(route_total.urls)),
]