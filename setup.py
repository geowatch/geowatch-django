#!/usr/bin/env python

from setuptools import setup

setup(
    name='geowatch-django',
    version='0.0.2',
    install_requires=[],
    author='GeoWatch Developers',
    author_email='geowatch.dev@gmail.com',
    license='BSD License',
    url='https://github.com/geowatch/geowatch-django/',
    keywords='python gis geowatch',
    description='Django app for integration of GeoWatch',
    long_description=open('README.md').read(),
    download_url="https://github.com/geowatch/geowatch-django/zipball/master",
    #py_modules=["geowatchdjango"],
    packages=["geowatchdjango"],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
