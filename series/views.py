from django.shortcuts import render
from django.http import HttpResponse
from utils.series_data import get_series

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
    {
        'title': 'asdf',
        'seasons': 7,
        'year': '2004'
    },
    {
        'title': 'asdf',
        'seasons': 7,
        'year': '2004'
    },
    {
        'title': 'asdf',
        'seasons': 7,
        'year': '2004'
    },
    {
        'title': 'asdf',
        'seasons': 7,
        'year': '2004'
    },
    {
        'title': 'asdf',
        'seasons': 7,
        'year': '2004'
    },
]
series = get_series()

def home(request):
    context = {
        'series_list': series
    }
    return render(request, 'series/series_homepage.html', context)