#!/usr/bin/python

BASE_URL = 'http://boxofficemojo.com'
DAILY_CHART = 'daily/chart'
WEEKEND_CHART = 'weekend/chart'
WEEKLY_CHART = 'weekly/chart'
# seconds to sleep between 2 consecutive page requests
INTERVAL_BETWEEN_REQUESTS = 1

from .bom import BOM
