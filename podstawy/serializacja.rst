Serializacja
============

Pickle
------

``json``
--------

.. code:: python

    import json
    json.loads()
    json.dumps()

    json.JSONEncoder.default = lambda self,obj: ('{:%Y-%m-%dT%H:%M:%S.%fZ}'.format(obj) if isinstance(obj, datetime.datetime) else None)



``csv``
-------

.. code:: python

    >>> import csv
    >>> with open('names.csv') as csvfile:
    ...     reader = csv.DictReader(csvfile)
    ...     for row in reader:
    ...         print(row['first_name'], row['last_name'])

.. code:: python

    >>> import csv

    >>> with open('names.csv', 'w') as csvfile:
    ...    fieldnames = ['first_name', 'last_name']
    ...    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    ...
    ...    writer.writeheader()
    ...    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    ...    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    ...    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})


.. code:: python

    >>> import csv

    >>> data = [
    ...    {'first_name': 'Baked', 'last_name': 'Beans'},
    ...    {'first_name': 'Lovely', 'last_name': 'Spam'},
    ...    {'first_name': 'Wonderful', 'last_name': 'Spam'}
    ...]

    >>> with open('names.csv', 'w') as csvfile:
    ...    fieldnames = data[0].keys()
    ...    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    ...    writer.writeheader()
    ...
    ...    for row in data:
    ...        writer.writerow(row)
    ...


xml
---
