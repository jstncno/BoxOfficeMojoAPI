#!/usr/bin/python

"""
Box Office Mojo API
Unofficial Python API for Box Office Mojo API.

Author: Justin Cano
Email: jcano001@ucr.edu
License: MIT
"""
import urllib2
import unittest
import vcr

from bs4 import BeautifulSoup
from bom import BOM, BASE_URL, WEEKEND_CHART
from test_utils import FIXTURES_DIR


class TestBOM(unittest.TestCase):

    def setUp(self):
        self.bom = BOM()

    @vcr.use_cassette(FIXTURES_DIR + '/vcr_cassettes/bom.yml')
    def test_bom(self):
        """
        Tests if response is in fact the weekend chart
        """
        movies = self.bom.get_movies()
        movie = movies.next()
        assert type(movie.this_week_rank) == int
        assert type(movie.last_week_rank) == int
        assert type(movie.title) == str
        assert type(movie.studio) == str
        assert type(movie.gross_str) == str
        assert ("$") in movie.gross_str
        assert type(movie.gross_int) == int


if __name__ == '__main__':
    unittest.main()


'''
with vcr.use_cassette(FIXTURES_DIR + '/vcr_cassettes/weekend_chart.yaml'):
    response = urllib2.urlopen('%s/%s' % (BASE_URL, WEEKEND_CHART)).read()
    assert 'Weekend Box Office' in response

soup = BeautifulSoup(response)
table = soup.findChildren('table')[4]
rows = soup.findChildren('tr')[6:-2]
name = rows[0].findChildren('td')[2]

print name

def get_movie_names():
    for i in range(len(rows)):
        yield rows[i].findChildren('td')[2]

if __name__ == '__main__':
    movies = get_movie_names()
'''
