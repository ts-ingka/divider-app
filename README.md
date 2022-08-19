# Amazing Divide Stuff Framework
**This is just a silly repo to experiment with deploying a package to PyPI and setting up good CI/CD practices**

 > Divide two numbers and even print the result.

[![PyPI Version][pypi-image]][pypi-url]
[![Build Status][build-image]][build-url]
[![][stars-image]][stars-url]
[![][versions-image]][versions-url]

<!-- Badges: -->

[pypi-image]: https://img.shields.io/pypi/v/divide-stuff
[pypi-url]: https://pypi.org/project/divide-stuff
[build-image]: https://github.com/ts-ingka/divider-app/actions/workflows/build.yml/badge.svg
[build-url]: https://github.com/ts-ingka/divider-app/actions/workflows/build.yml
[stars-image]: https://img.shields.io/github/stars/ts-ingka/divider-app/
[stars-url]: https://github.com/ts-ingka/divider-app
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
