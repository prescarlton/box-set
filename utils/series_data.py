"""Tools used to organize data of TV Series"""
# built-in imports
import os

# custom imports
from .library_settings import SERIES_DIRECTORY
from .scraping import scrape


def get_series_list():
    '''returns a list of strings containing names of all series in the library'''
    # list that will contain strings of the names of all of the series in the library
    series_titles = []
    for series_title in os.listdir(SERIES_DIRECTORY):
        series_titles.append(series_title)
    return series_titles


def get_series():
    '''returns a list of dictionaries of all series in the library'''

    # list that will contain dictionaries of all the series in the library
    series_list = []
    for series in get_series_list():
        # for each series we want to scrape all of the series' data.
        series_list.append(scrape(series, 'tv series'))

    return series_list
