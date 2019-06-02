from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

movies = [
    {
        'title': 'Weekend at Bernie\'s',
        'year': 'a while back'
    },
    {
        'title': 'weird bigfoot movie',
        'year': '2019'
    },
    {
        'title': 'Another AAA title',
        'year': '2018'
    },
]

def home(request):
    context = {
        'movies_list': movies
    }
    return render(request, "movies/movies_page.html", context)