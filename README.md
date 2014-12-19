BoxOfficeMojoAPI
================
![Build Status](https://travis-ci.org/hyperbit/BoxOfficeMojoAPI.svg?branch=master)

Unofficial Python API for [Box Office Mojo](http://boxofficemojo.com/).

#Usage
```python
from bom import BOM, DAILY_CHART

bom = BOM(chart=DAILY_CHART)

for movie in bom.get_chart(limit=10):
    print (movie.rank, movie.title, movie.gross)
```

#API
##`class BOM(chart=bom.DAILY_CHART)`
Get list of movies from Box Office Mojo. Available charts are:

```python
bom.DAILY_CHART
bom.WEEKEND_CHART
bom.WEEKLY_CHART
```

###attribute `BOM.date`
The chart date, represented as a datetime object
###`BOM.weekend_chart(limit=10)`
Get movies from top box office charts from the past weekend.
###`BOM.daily_chart(limit=10)`
Get movies from top box office charts for today.
##`class Movie()`
Movie model for Box Office Mojo
###attribute `Movie.movie_id`
The movie's ID on Box Office Mojo
###attribute `Movie.rank`
The movie's current rank
###attribute `Movie.title`
The title of the movie
###attribute `Movie.studio`
The movie's producing studio
###attribute `Movie.url`
The movie's URL on Box Office Movie
###attribute `Movie.gross`
The movie's gross income
Note: can be either weekend or daily gross, depending on which BOM method you called
###property `Movie.gross_val`
The movie's gross income, represented as an integer
###`Movie.weekend_trend()`
Get the movie's weekend trend as a list of tuples
###`Movie.daily_trend()`
Get the movie's daily trend as a list of tuples
(daily trend may be unavailable)


#Unit Tests
To run the test suite, fork the project and set up the run script locally.

First, you will probably need to install the dependencies:
```bash
$ pip install -r requirements.txt
```

Then, locally set up the run script and run:
```bash
$ chmod 777 ./runtests.sh
$ ./runtests.sh
```

To run individual tests:
```bash
$ python -m unittest tests.<module name>
```

The first time you run these tests, the test suite will create a [VCR.py](https://github.com/kevin1024/vcrpy) cassette into `tests/fixtures/vcr_cassettes`, which records and saves any HTTP requests stubs made by the unittests. Any subsequent test runs will use the cassette instead of make another HTTP request.
