from django.shortcuts import render
from django.http import HttpResponse
from utils.series_data import get_series, refresh_series

series = get_series()

def home(request):
    context = {
        'series_list': series,
        'reload': refresh_series()
    }
    return render(request, 'series/series_homepage.html', context)