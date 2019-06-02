from django.shortcuts import render
from django.http import HttpResponse

series = [
    {
        'title': 'Game of Thrones',
        'seasons': 8,
        'year': '2005'
    },
    {
        'title': 'Supernatural',
        'seasons': 14,
        'year': '2002'
    },
    {
        'title': 'Psych',
        'seasons': 7,
        'year': '2004'
    },
]

def home(request):
    context = {
        'series_list': series
    }
    return render(request, 'series/series_page.html', context)