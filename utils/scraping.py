"""Module containing all the scraping functionality"""
# built-in imports
import os
import requests
import ast
# 3rd party imports
from bs4 import BeautifulSoup
# custom imports
from .library_settings import DATA_DIRECTORY, SERIES_DIRECTORY, MOVIES_DIRECTORY

from bs4 import BeautifulSoup


def scrape_series(series_name):
    '''
    uses bs4 to scrape a TVDB page and returns a dictionary of the series's info
    '''
    display_name = series_name
    num_seasons = 0
    # gotta convert that bad boy to a url 
    series_name = series_name.replace('\'', '')
    series_name = series_name.replace('.', '-')
    series_name = series_name.lower().replace(' ', '-')
    series_name = series_name.lower().replace("'", "")
    series_name = series_name.lower().replace("!","")

    series_url = "https://www.thetvdb.com/series/" + series_name

    series_request = requests.get(series_url)

    try:
        series_html = BeautifulSoup(series_request.text, 'html.parser')
        
        seasons_url = series_url + "/seasons/all"
        seasons_request = requests.get(seasons_url)
        
        seasons_html = BeautifulSoup(seasons_request.text, 'html.parser')

        series_desc = series_html.find('div', attrs={'class': 'change_translation_text', 'data-language': 'en'}).text.strip()
        
        artwork_request = requests.get(series_url + '/artwork/poster')
        artwork_html = BeautifulSoup(artwork_request.text, 'html.parser')
        series_poster = artwork_html.find('img', attrs={'class': 'media-object'})["src"]

        # used to get genre, year, and other 'basic info'
        series_basic_info = series_html.find('div', attrs={'id':'series_basic_info'})
        year_produced = series_basic_info.findAll('span')[2].text.split('-')[0]
        series_genres = series_basic_info.findAll('span')[5].text.split(', ')
        
    except Exception as e:
        print(e)
        return display_name

    # seasons info
    for season in seasons_html.find_all('h3'):
        plain_text = season.text.strip()
        if not plain_text.lower() == "specials":
            num_seasons += 1

    # logic to make sure that the series description ain't too long
    if len(series_desc) > 175:
        short_desc = series_desc[0:150] + '...'
    else:
        short_desc = series_desc
    # logic to make sure that the series title ain't too long (foster's home for imaginary friends)
    if len(display_name) > 25:
        short_name = display_name[0:22] + '...'
    else:
        short_name = display_name

    return {
        "title": display_name,
        "display_title": short_name,
        "year": year_produced,
        "seasons": num_seasons,
        "description": series_desc,
        "genres": series_genres,
        "image": series_poster,
        "short_description": short_desc
    }


def scrape_movie(movie_name):
    """tool to scrape data for a movie"""
    # pls actually write this
    return {
        'title': "Weekend at Bernie's",
        'year': 1989,
        'description': "Two friends are invited for a weekend to a luxury island with their boss. The boss gets shot and nobody seems to notice, except for the two friends. In order not to become suspects of murder they treat the body as a puppet and make people believe he's still alive. The killer wants to do his job so when he is informed that the stiff is still alive he's got to shoot him again, and again, and again.",
        'genre': ['COMEDY'],
        'tags': ['beach', 'mission of murder', 'boss', 'bad boss', 'house'],
        'image': 'https://image.tmdb.org/t/p/w600_and_h900_bestv2/h3hjMREZEUPtDkZBiYDzLq0THk0.jpg'
    }


def scrape(media_title, media_type, force_refresh=False):
    """return the information for a series/movie as a dictionary"""
    
    # if there isn't a file for the media locally
    if f'{media_title}.txt' not in os.listdir(DATA_DIRECTORY + f'/{media_type}' ):
        # scrape that bad boy
        if media_type == 'tv series':
            media_data = scrape_series(media_title)

            # create the data file for the show 
            with open(DATA_DIRECTORY + f'/{media_type}/{media_title}.txt', 'w') as data_file:
                data_file.write(str(media_data))
                


        elif media_type == 'movie':
            media_data = scrape_movie(media_title) 
        
    else:

        with open(DATA_DIRECTORY + f'/{media_type}/{media_title}.txt', 'r') as data_file:
            media_data = eval(data_file.read())


    return media_data
        