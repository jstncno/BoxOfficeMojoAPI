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
#name = table.findChildren('td')[2]
print rows[len(rows)-1]


#def get_soup(page=WEEKEND_CHART):
#	content = requests.get('%s/%s' % (BASE_URL, page)).text
#	print BeautifulSoup(content)


#if __name__ == '__main__':
#	get_soup()
