#!/usr/bin/python

"""
Box Office Mojo API
Unofficial Python API for Box Office Mojo API.

Author: Justin Cano
Email: jcano001@ucr.edu
License: MIT
"""
import urllib
import urllib2
import re
#import requests
from bs4 import BeautifulSoup
from .constants import BASE_URL, WEEKEND_CHART

def get_soup(page=WEEKEND_CHART):
    #content = requests.get('%s/%s/' % (BASE_URL, page))
    content = urllib2.urlopen('%s/%s' % (BASE_URL, page)).read()
    return BeautifulSoup(content)

class BOM(object):
    """
    The class that parses the BoxOfficeMojo page, and builds up all the movies
    """

    def _get_movie_id(self, movie_id_link):
        """
        Returns the id from movie_id_link
        """
        return re.sub('\/movies\/\?id\=', '', movie_id_link)


    def get_movies(self, chart=WEEKEND_CHART, limit=10):
        """
        Yields a list of box office movies from chart of BoxOfficeMojo

        'limit' is the max number of movies to return.
        Default is 10, cannot be more than 25.
        """
        if limit <= 0 or limit > 25:
            limit = 25

        movies_found = 0

        #while movies_found < limit:
        soup = get_soup(chart)
        movies = soup.findChildren('tr')[6:-2]
        for m in movies:
            attrs = m.findChildren('td')
            rank = int(attrs[0].string)
            title = str(attrs[2].string)
            movie_id = self._get_movie_id(str(attrs[2].a['href']))
            studio = str(attrs[3].string)
            gross_str = str(attrs[4].string)
            gross_int = int(gross_str[1:].replace(',', ''))

            movie = Movie(movie_id, rank, title, studio, gross_str, gross_int)
            yield movie
            movies_found += 1

            if movies_found >= limit:
                return



class Movie(object):
    """
    Movie class that represents a movie on BoxOfficeMojo
    """
    def __init__(self, movie_id, rank, title, studio, gross_str, gross_int):
        self.movie_id = movie_id # the movie's ID on BoxOfficeMojo.com
        self.rank = rank # this week's rank
        self.title = title # the title of the movie
        self.studio = studio # the movie's producing studio
        self.gross_str = gross_str # movie's gross income (str)
        self.gross_int = gross_int # movie's gross income (int)

    def weekend_trend(self):
        """
        Returns a list of tuples of the Movie's weekend trend data
        Return value:
        [(week_number, date, rank, weekend_gross),]
        """
        params = {
            'page':'weekend',
            'id':self.movie_id
        }
        encoded_params = urllib.urlencode(params)
        page = '/movies/?' + encoded_params
        soup = get_soup(page)
        table = soup.findChildren('table')[6]
        # sometimes the page will have an extra IMDb advertisement
        # skip to the next table if such element exists
        if 'imdb' in table.a['href']:
            table = soup.findChildren('table')[7]
        rows = table.findChildren('tr')[1:]
        
        weekend = []
        rank = []
        gross = []
        index = []
        for row in rows:
            td = row.findChildren('td')
            weekend.append(td[0].string.encode('raw_unicode_escape').replace('\x96', '-'))
            rank.append(str(td[1].string))
            gross.append(str(td[2].string))
            index.append(int(td[8].string))

        return zip(index, weekend, rank, gross)



if __name__ == '__main__':
    get_soup()
