Getting Started!
================

First, install geowatch-django and geowatch-util via pip.


Client
------

**File Store**

.. code-block:: python

    provision_geowatch_client()

Consumers
------

**File Store**

.. code-block:: python

    provision_geowatch_consumer(
        topic,
        codec,
        max_tries=12,
        sleep_period=5,
        topic_check=False,
        verbose=False)

Producers
-------

.. code-block:: python

    provision_geowatch_producer(
        topic,
        codec,
        client=None,
        max_tries=12,
        sleep_period=5,
        topic_check=False,
        verbose=False)
