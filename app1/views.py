from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def movie_name(request):
    return HttpResponse('<h1>Movie name--> Harry Potter and Sorcere\'s stone<h1><hr/>')


def year(request):
    return HttpResponse('<h1>Released year--> 2001<h1><hr/>')