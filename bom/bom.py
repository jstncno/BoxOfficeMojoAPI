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

	def get_movies(self, chart=WEEKEND_CHART, limit=10):
		"""
		Yields a list of box office movies from chart of BoxOfficeMojo

		'limit' is the max number of movies to return.
		Default is 10, cannot be more than 25.
		"""
		#
		if limit <= 0 or limit > 25:
			limit = 25

		movies_found = 0

		#while movies_found < limit:
		soup = get_soup(chart)
		table = soup.findChildren('table')[4]
		movies = soup.findChildren('tr')[6:-2]
		for m in movies:
			attrs = m.findChildren('td')
			tw = int(attrs[0].string)
			lw = int(attrs[1].string)
			title = str(attrs[2].string)
			studio = str(attrs[3].string)
			gross_str = str(attrs[4].string)
			gross_int = int(gross_str[1:].replace(',',''))

			movie = Movie(tw, lw, title, studio, gross_str, gross_int)
			yield movie
			movies_found += 1

			if movies_found >= limit:
				return



class Movie(object):
	"""
	Movie class that represents a movie on BoxOfficeMojo
	"""
	pass
	def __init__(self, this_week_rank, last_week_rank, title, studio,
				 gross_str, gross_int):
		self.this_week_rank = this_week_rank # this week's rank
		self.last_week_rank = last_week_rank # last week's rank
		self.title = title # the title of the movie
		self.studio = studio # the movie's producing studio
		self.gross_str = gross_str # movie's gross income (str)
		self.gross_int = gross_int # movie's gross income (int)




if __name__ == '__main__':
	get_soup()
