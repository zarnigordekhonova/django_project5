from django.urls import path
from app2.views import movie_rating, movie_language


urlpatterns = [
    path('rating', movie_rating),
    path('language', movie_language)
]