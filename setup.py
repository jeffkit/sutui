#!/usr/bin/env python

from setuptools import setup, find_packages
from sutui import VERSION

url="https://github.com/jeffkit/sutui"

long_description="Sutui Python SDK"

setup(name="sutui",
      version=VERSION,
      description=long_description,
      maintainer="jeff kit",
      maintainer_email="bbmyth@gmail.com",
      url = url,
      long_description=long_description,
      packages=find_packages('.'),
     )


