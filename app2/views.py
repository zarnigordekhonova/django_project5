from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def movie_language(request):
    return HttpResponse('<h1>Movie language--> English<h1><hr/>')


def movie_rating(request):
    return HttpResponse('<h1>Movie rating(ImDB)--> 7.6/10<h1><hr/>')
