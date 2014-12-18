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
from bom import BOM
from test_utils import FIXTURES_DIR


class TestMovie(unittest.TestCase):

    @vcr.use_cassette(FIXTURES_DIR + '/vcr_cassettes/movie.yaml')
    def setUp(self):
        self.bom = BOM()
        self.movies = self.bom.get_chart()
        self.test_movie = self.movies.next() # get the first movie for testing

    def test_movie(self):
        assert type(self.test_movie.gross_val) == int



if __name__ == '__main__':
    unittest.main()
