BoxOfficeMojoAPI
================

Unofficial Python API for [Box Office Mojo](http://boxofficemojo.com/).

#Usage
```python
from bom import BOM

bom = BOM()

for movie in bom.weekend_chart(limit=10):
    print (movie.rank, movie.title, movie.gross_str)
```

#API
##class BOM()
Get list of movies from Box Office Mojo
###BOM.weekend_chart(limit=10)
Get movies from top box office charts from the past weekend.
###BOM.daily_chart(limit=10)
Get movies from top box office charts since the beginning of the week.
##class Movie()
Movie model for Box Office Mojo
###attribute Movie.movie_id
The movie's ID on Box Office Mojo
###attribute Movie.rank
The movie's current rank
###attribute Movie.title
The title of the movie
###attribute Movie.studio
The movie's producing studio
###attribute Movie.gross
The movie's gross income
###property Movie.gross_val
The movie's gross income, represented as an integer
###Movie.weekend_trend()
Get the movie's weekend trend as a list of tuples
###Movie.daily_trend()
Get the movie's daily trend as a list of tuples


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
