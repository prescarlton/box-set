from bs4 import BeautifulSoup
import requests


soup = BeautifulSoup('https://www.thetvdb.com/series/the-walking-dead')
print(soup.prettify)