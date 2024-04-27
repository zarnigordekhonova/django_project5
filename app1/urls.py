from django.urls import path
from app1.views import movie_name, year


urlpatterns = [
    path('name', movie_name),
    path('year', year)
]