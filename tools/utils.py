# tools to turn a list of shows into a directory
# 1. take list of shows as input
# 2. remove bad characters and newline characters
# 3. parse lines to get show name, year of production, and num of seasons
# 4. create dictionary entry for each show
# 5. create parent dirs in /shows/
# 6. for each show, create a .txt containing info about the show
# 7. for each show, create a sub directory for each season
# 8. for each season, create a .txt containing info about what episodes
#    have been downloaded

import os
import scraper
# list of characters to be removed from show names
badchars = ['\\', '?', '>', '<', '|', '"', '*', ':']
# dictionary for all shows
shows = {}
# location where shows are stored
SHOWS_LOCATION = "F:/media/shows"


def clean(file):
    '''
    takes file as input and 'cleans' it by
    removing all invalid characters from the file so
    that the names can be used in file explorer, and then sorts it
    '''
    with open(file, 'r') as f:
        lines = f.readlines()

    lines = [line for line in lines if line != '' and line != '\n']

    for i, line in enumerate(lines):
        for oof in badchars:
            lines[i] = lines[i].replace(oof, '')
    lines.sort()
    with open(file, 'w') as f:
        for line in lines:
            f.write(line)


def makeShowList(file):
    '''
    makes a list of shows from file
    '''
    with open(file, 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        lines[i] = line.strip()

    lines.sort()
    return lines


def getShows(showlist):
    '''
    takes list of shows as input and returns a dictionary with shows and
    their information
    '''
    for show in showlist:
        show_name = show.split('//')[0]
        year = show.split('//')[1]
        num_seasons = int(show.split('//')[2])

        shows[show_name] = {
            "year": year,
            "seasons": num_seasons
        }


def showInfo(show_name):
    '''
    returns a pretty, formatted blurb of information containing
    data scraped from TVDB
    '''
    pass


def createShowDirectories():
    '''
    creates directories for all shows in the given list
    (this typically is a list generated from a .txt file)
    '''

    for show in shows:
        try:
            show_dict = scraper.scrapeSeries(show)
        except Exception as e:
            print("could not scrape data for %s. skipping for now." % (show))
            print(e)
            continue

        dir_name = show
        if (os.path.exists(f'{SHOWS_LOCATION}/{dir_name}')):
            # os.makedirs('../shows/' + dir_name)
            with open(f'{SHOWS_LOCATION}/{dir_name}/show.txt', 'w') as f:
                f.write(str(show_dict))
                # f.write(showInfo(show))


def createSeasonFolders():
    '''
    creates folders for all the seasons in a show
    '''
    for series in shows:

        num_seasons = int(shows[series]["seasons"])

        for i in range(num_seasons):
            if not(os.path.exists(f'{SHOWS_LOCATION}/{series}/Season {str(i + 1)}')):

                os.makedirs(f'{SHOWS_LOCATION}/{series}/Season {str(i + 1)}')
                # create file containing season information
                with open(f'{SHOWS_LOCATION}/{series}/Season {str(i + 1)}/season.txt', 'w') as f:
                    f.write('yeet i should make this do something')


def createMasterFile():
    '''
    creates a textfile in the top level directory of the shows to store
    information about shows as a whole, such as being downloaded/found etc.
    '''
    pass


def reloadShowFiles():
    '''
    creates all the .txt files containing a show's information
    '''
    for show in os.listdir('../shows/'):

        # year = shows[show]['year']
        # num_seasons = shows[show]['seasons']
        # owned_seasons = 0

        for season in os.listdir(f'{SHOWS_LOCATION}/shows/{show}'):
            num_eps = 0

            for _, dirnames, episodes in os.walk('../shows/%s/%s' % (show, season)):
                num_eps += len(episodes)

            if num_eps > 0:
                print("yeet i have episodes for season " + season)

            print('season:'+season)


getShows(makeShowList('../tv.txt'))
createShowDirectories()
createSeasonFolders()
print(shows)
# reloadShowFiles()
# fosters = scraper.scrapeSeries("Foster's Home for Imaginary Friends")

