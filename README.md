BoxOfficeMojoAPI
================

Unofficial Python API for [Box Office Mojo](http://boxofficemojo.com/).

#Usage
```python
from bom import BOM, WEEKEND_CHART

bom = BOM()

for movie in bom.get_movies(chart=WEEKEND_CHART, limit=10):
  print movie.title
```
