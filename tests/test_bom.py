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


class TestBOM(unittest.TestCase):

    @vcr.use_cassette(FIXTURES_DIR + '/vcr_cassettes/bom.yaml')
    def setUp(self):
        self.bom = BOM()
        self.movies = self.bom.get_chart()

    def test_bom(self):
        assert type(self.bom.date) == str


if __name__ == '__main__':
    unittest.main()
