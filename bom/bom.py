#!/usr/bin/python

"""
Box Office Mojo API
Unofficial Python API for Box Office Mojo.

Author: Justin Cano
Email: jcano001@ucr.edu
License: MIT
"""
import urllib
import urllib2
import re
import datetime

from bs4 import BeautifulSoup
from .constants import BASE_URL, WEEKEND_CHART, DAILY_CHART, WEEKLY_CHART

def get_soup(page=WEEKEND_CHART):
    #content = requests.get('%s/%s/' % (BASE_URL, page))
    content = urllib2.urlopen('%s/%s' % (BASE_URL, page)).read()
    return BeautifulSoup(content)

class BOM(object):
    """
    The class that parses the BoxOfficeMojo page, and builds up all the movies
    """
    def __init__(self, chart=DAILY_CHART):
        self._chart = chart
        self.soup = get_soup(self._chart)
        if chart == WEEKLY_CHART:
            self._date = self.soup.findChildren('h2')[1].string
        elif chart == WEEKEND_CHART:
            self._date = self.soup.findChildren('b')[2].string
        else:
            self._date = self.soup.findChildren('b')[12].br.string

    def _get_movie_id(self, movie_id_link):
        """
        Returns the id from movie_id_link
        """
        #return re.sub('\/movies\/\?id\=', '', movie_id_link)
        return movie_id_link.split('id=')[1]

    def get_chart(self, limit=10):
        """
        Yields a list of box office movies from the chart of BoxOfficeMojo
        specified by self._chart

        'limit' is the max number of movies to return.
        Default is 10, cannot be more than 25.
        """
        if limit <= 0 or limit > 25:
            limit = 25

        movies_found = 0

        if self._chart == DAILY_CHART:
            movies = self.soup.findChildren('tr')[16:-2]

            s = self.soup.findChildren('b')
            mvs = s[13:len(s)-3]

            # if today's charts are not yet available...
            # shift our collection up one
            if "$" not in mvs[0]:
                mvs = s[14:len(s)-3]

            it = iter(mvs)
            mvs = zip(it, it)

            assert len(mvs) == len(movies)

            for (i, m) in enumerate(movies):
                attrs = m.findChildren('td')
                rank = str(attrs[0].string)
                movie_id = self._get_movie_id(str(attrs[1].b.a['href']))
                studio = str(attrs[1].small.a.string)

                title = str(mvs[i][0].next_element.string)
                gross = str(mvs[i][1].next_element.string)

                movie = Movie(movie_id, rank, title, studio, gross)
                yield movie
                movies_found += 1

                if movies_found >= limit:
                    return

        elif self._chart == WEEKEND_CHART or self._chart == WEEKLY_CHART:
            table = self.soup.findChildren('table')[4]
            movies = table.findChildren('tr')[1:-1]
            
            for m in movies:
                attrs = m.findChildren('td')
                rank = str(attrs[0].string)
                title = str(attrs[2].string)
                movie_id = self._get_movie_id(str(attrs[2].a['href']))
                studio = str(attrs[3].string)
                gross = str(attrs[4].string)

                movie = Movie(movie_id, rank, title, studio, gross)
                yield movie
                movies_found += 1

                if movies_found >= limit:
                    return

        return

    @property
    def date(self):
        if self._chart != DAILY_CHART:
            return str(self._date)
        else:
            today = datetime.datetime.today()
            year = today.strftime("%Y")
            date_str = "%s/%s" % (self._date, year)
            date = datetime.datetime.strptime(date_str, "%m/%d/%Y")

            if today < date:
                year = (today - datetime.timedelta(years=1)).strftime("%Y")
                date_str = "%s/%s" % (self._date, year)
                date = datetime.datetime.strptime(date_str, "%m/%d/%Y")

            return date.strftime('%B %d, %Y')

class Movie(object):
    """
    Movie class that represents a movie on BoxOfficeMojo
    """

    def _get_movie_soup(self, page='', view=''):
        params = {
            'page':page,
            'view':view,
            'id':self.movie_id
        }
        encoded_params = urllib.urlencode(params)
        page = '/movies/?' + encoded_params
        return get_soup(page)

    def _get_domestic_total(self):
        soup = self._get_movie_soup()
        center = soup.findChildren('center')[0]
        return str(center.findChildren('tr')[0].b.string)


    def __init__(self, movie_id, rank, title, studio, gross):
        self.movie_id = movie_id # the movie's ID on BoxOfficeMojo.com
        self.rank = rank # this week's rank
        self.title = title # the title of the movie
        self.studio = studio # the movie's producing studio
        self.gross = gross # movie's gross income (can be either be weekend or daily)
        self.gross_to_date = self._get_domestic_total()

    def get_trend(self, chart=DAILY_CHART):
        """
        Returns a list of tuples of the Movie's trend data
        specified by @chart
        Return value:
        [(week_number, date, rank, weekend_gross),]
        """
        if chart == DAILY_CHART:
            soup = self._get_movie_soup(page='daily',view='chart')
            center = soup.findChildren('center')[1]
            table = center.findChildren('table')[0]
            rows = table.findChildren('tr')[1:]

            day = []
            rank = []
            gross = []
            index = []
            for row in rows:
                td = row.findChildren('td')
                try:
                    d = str(td[1].string)
                    r = str(td[2].string)
                    g = str(td[3].string)
                    i = str(td[9].string)
                except:
                    pass
                finally:
                    day.append(d)
                    rank.append(r)
                    gross.append(g)
                    index.append(i)

            return zip(index, day, rank, gross)

        elif chart == WEEKEND_CHART or chart == WEEKLY_CHART:
            soup = self._get_movie_soup('weekend')
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
                index.append(str(td[8].string))

            return zip(index, weekend, rank, gross)

        return []

    @property
    def gross_val(self):
        try:
            return int(self.gross[1:].replace(',', ''))
        except ValueError: # gross may not be available at the moment
            return 0

if __name__ == '__main__':
    get_soup()
