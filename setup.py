#!/usr/bin/env python

from setuptools import setup, find_packages

url = "https://github.com/jeffkit/sutui"

long_description = "Sutui Python SDK"

setup(name="sutui",
      version=0.3,
      description=long_description,
      maintainer="jeff kit",
      maintainer_email="bbmyth@gmail.com",
      url=url,
      long_description=long_description,
      packages=find_packages('.'),
      insatll_requires=[
          'requests',
          ])
