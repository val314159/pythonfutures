#!/usr/bin/env python

from distutils.core import setup

setup(name='futures',
      version='0.1',
      description='Java-style futures implementation in Python',
      author='Brian Quinlan',
      author_email='brian@sweetapp.com',
      url='http://code.google.com/p/pythonfutures',
      download_url='http://pypi.python.org/pypi/futures/',
      packages=['futures'],
      license='BSD',
      classifiers=['License :: OSI Approved :: BSD License',
                   'Development Status :: 3 - Alpha',
                   'Intended Audience :: Developers',
                   'Programming Language :: Python :: 2']
      )