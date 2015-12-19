GeoWatch Django (geowatch-django)
==========

.. image:: https://travis-ci.org/geowatch/geowatch-django.png
    :target: https://travis-ci.org/geowatch/geowatch-django

.. image:: https://img.shields.io/pypi/v/geowatch-django.svg
    :target: https://pypi.python.org/pypi/geowatch-django

.. image:: https://readthedocs.org/projects/geowatch-django/badge/?version=master
        :target: http://geowatch-django.readthedocs.org/en/latest/
        :alt: Master Documentation Status

Description
-----------

Django integration library for GeoWatch, a spatially-enabled distributed message broker.

Installation
------------

.. code-block:: bash

    pip install git+git://github.com/geowatch/geowatch-django.git@master


Usage
-----

Add the following to INSTALLED_APPS in settings.py:

.. code-block:: bash

    'geowatchdjango'

Also, include the following new variables in settings.py:

.. code-block:: bash

    AWS_ACCESS_KEY_ID = ""  # Used by AWS Kinesis
    AWS_SECRET_ACCESS_KEY = ""  # Used by AWS Kinesis

    GEOWATCH_ENABLED = True  # or False
    GEOWATCH_STREAMING_BACKEND = "kinesis"  # or "kafka"
    GEOWATCH_TOPIC_PREFIX= "geowatch-"  # Assigned to GeoWatch Client and prefixs all topics sent to server
    GEOWATCH_KINESIS_REGION = "us-east-1"  # Used by AWS Kinesis
    GEOWATCH_HOST = "localhost:9092"  # Used by Apache Kafka

Contributing
------------

We are currently accepting pull requests for this repository. Please provide a human-readable description with a pull request and update the README.rst file as needed.

License
-------

Copyright (c) 2015, Patrick Dufour
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of geowatch-django nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
