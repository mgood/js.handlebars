#!/usr/bin/python

import setuptools
from setuptools import find_packages
from glob import glob
setuptools.setup(
  name = 'js.handlebars',
  version = '1.0.0.rc.3',
  license = 'BSD',
  description = 'Fanstatic package for Handlebars.js',
  long_description = open('README.txt').read(),
  author = 'Jacco Taal',
  author_email = 'j@jaccotaal.nl',
  url = 'http://github.com/jrtaal/js.handlebars/',
  platforms = 'any',
  packages=find_packages(),
  namespace_packages=['js'],
  include_package_data=True,
  data_files = [('js/handlebars/resources',glob('js/handlebars/resources/*.js'))],
  zip_safe = False,
  install_requires=[
    'fanstatic',
  ],
  entry_points={
    'fanstatic.libraries': [
      'handlebars = js.handlebars:library',
    ],
  },
)
