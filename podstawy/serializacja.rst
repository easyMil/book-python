Serializacja
============

Pickle
------

``json``
--------

.. code:: python

    >>> import json

    >>> json.loads()

Problem z rzutowaniem daty na JSON:

    >>> json.JSONEncoder.default = lambda self,obj: ('{:%Y-%m-%dT%H:%M:%S.%fZ}'.format(obj) if isinstance(obj, datetime.datetime) else None)

    >>> json.dumps()


``csv``
-------

.. code:: python

    >>> import csv

    >>> with open('filename.csv') as csvfile:
    ...     data = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    ...
    ...     for row in data:
    ...         print(row['first_name'], row['last_name'])


.. code:: python

    >>> import csv

    >>> data = [
    ...    {'first_name': 'Baked', 'last_name': 'Beans'},
    ...    {'first_name': 'Lovely', 'last_name': 'Spam'},
    ...    {'first_name': 'Wonderful', 'last_name': 'Spam'}
    ...]

    >>> with open('filename.csv', 'w') as csvfile:
    ...    fieldnames = data[0].keys()
    ...    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',', quotechar='"')
    ...    writer.writeheader()
    ...
    ...    for row in data:
    ...        writer.writerow(row)
    ...


xml
---
