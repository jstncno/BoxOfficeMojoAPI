#!/usr/bin/python

"""
Box Office Mojo API
Unofficial Python API for Box Office Mojo API.

Author: Justin Cano
Email: jcano001@ucr.edu
License: MIT
"""
import requests
from bs4 import BeautifulSoup
from constants import BASE_URL, WEEKEND_CHART

import vcr
import urllib2

with vcr.use_cassette('fixtures/vcr_cassettes/weekend_chart.yaml'):
    #response = str(requests.get('%s/%s' % (BASE_URL, WEEKEND_CHART)).text)
    response = urllib2.urlopen('%s/%s' % (BASE_URL, WEEKEND_CHART)).read()
    assert 'Weekend Box Office' in response

soup = BeautifulSoup(response)
table = soup.findChildren('table')[4]
rows = soup.findChildren('tr')[6:-2]
name = rows[0].findChildren('td')[2]


def get_movie_names():
    for i in range(len(rows)):
        yield rows[i].findChildren('td')[2]



if __name__ == '__main__':
    movies = get_movie_names()
