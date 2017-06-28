#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='pyPandasMongo',
    version='0.0.2',
    packages=find_packages(include=["pyPandasMongo*"]),
    author='Thomas Schmelzer',
    author_email='thomas.schmelzer@gmail.com',
    description='', install_requires=['pandas>=0.20.0', 'pymongo', 'mongoengine']
)
