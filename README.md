# Amazing Divide Stuff Framework
**This is just a silly repo to experiment with deploying a package to PyPI and setting up good CI/CD practices**

 > Easily extend JSON to encode and decode arbitrary Python objects.

[![PyPI Version][pypi-image]][pypi-url]
[![Build Status][build-image]][build-url]
[![][stars-image]][stars-url]
[![][versions-image]][versions-url]

...

<!-- Badges: -->

[pypi-image]: https://img.shields.io/pypi/v/divide-stuff
[pypi-url]: https://pypi.org/project/divide-stuff
[build-image]: https://github.com/ts-ingka/divide-stuff/actions/workflows/build.yaml/badge.svg
[build-url]: https://github.com/ts-ingka/divide-stuff/actions/workflows/build.yaml
[stars-image]: https://img.shields.io/github/stars/ts-ingka/divide-stuff/
[stars-url]: https://github.com/ts-ingka/divide-stuff
[versions-image]: https://img.shields.io/pypi/pyversions/divide-stuff/
[versions-url]: https://pypi.org/project/divide-stuff/

It will quite literally divide stuff for you.

## How to use
```
from divide_stuff import Divider

divider = Divider()
divider.divide_numbers_print(20, 10)

result = divider.divide_numbers(20, 10)

# Amazing!!
```
