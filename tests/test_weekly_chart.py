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
from bom import BOM, BASE_URL, WEEKEND_CHART, WEEKLY_CHART
from test_utils import FIXTURES_DIR


class TestWeeklyChart(unittest.TestCase):

    @vcr.use_cassette(FIXTURES_DIR + '/vcr_cassettes/weekly_chart.yaml')
    def setUp(self):
        self.bom = BOM(WEEKLY_CHART)
        self.movies = self.bom.get_chart()
        self.test_movie = self.movies.next() # get the first movie for testing

    def test_weekly_chart(self):
        """
        Tests if BOM holds appropriate Movie objects
        """
        assert type(self.test_movie.rank) == str
        assert type(self.test_movie.title) == str
        assert type(self.test_movie.studio) == str
        assert type(self.test_movie.gross) == str
        assert "$" in self.test_movie.gross

    @vcr.use_cassette(FIXTURES_DIR + '/vcr_cassettes/weekly_trend.yaml')
    def test_weekly_trend(self):
        """
        Tests for the weekend trend of a movie
        """
        for movie in self.movies:
            trend_data = movie.get_trend(WEEKLY_CHART)
            assert len(trend_data) > 0
            assert type(trend_data) == list
            for data in trend_data:
                assert type(data) == tuple

if __name__ == '__main__':
    unittest.main()
