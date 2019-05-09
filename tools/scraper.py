import requests
from boxset_exceptions import InvalidSeriesURL
from bs4 import BeautifulSoup


def scrapeSeries(series_name):
    '''
    uses bs4 to scrape a TVDB page and returns a dictionary of the series's info
    '''
    display_name = series_name
    num_seasons = 0
    series_name = series_name.replace('\'', '')
    series_name = series_name.replace('.', '-')
    series_name = series_name.lower().replace(' ', '-')

    series_url = "https://www.thetvdb.com/series/" + series_name

    series_request = requests.get(series_url)
    print("Reponse Code %s for %s" % (series_request.status_code, series_name))
    print("parsing html...")

    try:
        series_html = BeautifulSoup(series_request.text, 'html.parser')

        seasons_url = series_url + "/seasons/all"
        seasons_request = requests.get(seasons_url)

        seasons_html = BeautifulSoup(seasons_request.text, 'html.parser')

        series_desc = series_html.find('div', attrs={'class': 'change_translation_text', 'data-language': 'en'}).text.strip()

        series_image = series_html.find('img', attrs={'class': 'img-responsive full_width_image'})['src']
    except:
        return series_name



    # seasons info
    for season in seasons_html.find_all('h3'):
        plain_text = season.text.strip()
        if not plain_text.lower() == "specials":
            num_seasons += 1

    show_dict = {
        "display_name": display_name,
        "seasons": num_seasons,
        "desc": series_desc,
        "series_image": series_image
    }
    return show_dict
