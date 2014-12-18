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
import unittest
import vcr

from bs4 import BeautifulSoup
from bom import BOM, BASE_URL, WEEKEND_CHART
from test_utils import FIXTURES_DIR


class TestWeekendChart(unittest.TestCase):

    @vcr.use_cassette(FIXTURES_DIR + '/vcr_cassettes/weekend_chart.yaml')
    def setUp(self):
        self.bom = BOM(WEEKEND_CHART)
        self.movies = self.bom.get_chart()
        self.test_movie = self.movies.next() # get the first movie for testing

    def test_weekend_chart(self):
        """
        Tests if BOM holds appropriate Movie objects
        """
        assert type(self.test_movie.rank) == str
        assert type(self.test_movie.title) == str
        assert type(self.test_movie.studio) == str
        assert type(self.test_movie.gross) == str
        assert "$" in self.test_movie.gross
        

    @vcr.use_cassette(FIXTURES_DIR + '/vcr_cassettes/weekend_trend.yaml')
    def test_weekend_trend(self):
        """
        Tests for the weekend trend of a movie
        """
        for movie in self.movies:
            trend_data = movie.get_trend(WEEKEND_CHART)
            assert len(trend_data) > 0
            assert type(trend_data) == list
            for data in trend_data:
                assert type(data) == tuple





if __name__ == '__main__':
    unittest.main()
