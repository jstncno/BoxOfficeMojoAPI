#!/usr/bin/python

"""
Box Office Mojo API
Unofficial Python API for Box Office Mojo API.

Author: Justin Cano
Email: jcano001@ucr.edu
License: MIT
"""
import urllib2
import re
import requests
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
	def get_movies(self, chart=WEEKEND_CHART, limit=10):
		"""
		Yields a list of box office movies from chart of BoxOfficeMojo
		"""
		movies_found = 0

		#while movies_found < limit:
		soup = get_soup(chart)
		table = soup.findChildren('table')[4]
		rows = soup.findChildren('tr')[6:-2]
		name = rows[0].findChildren('td')[2]
		#print name.findChildren('b')





if __name__ == '__main__':
	get_soup()
