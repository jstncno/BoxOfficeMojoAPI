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
from .constants import BASE_URL, WEEKEND_CHART

def get_soup(page=WEEKEND_CHART):
	content = requests.get('%s/%s' % (BASE_URL, page)).text
	print BeautifulSoup(content)


if __name__ == '__main__':
	get_soup()
