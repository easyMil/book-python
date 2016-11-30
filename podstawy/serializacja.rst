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

``csv``
-------

.. code:: python

    import csv

    FIELDNAMES = ['id', 'username', 'address']


    with open(FILENAME) as file:
        for row in csv.DictReader(file, delimiter=' ', quotechar='"', fieldnames=FIELDNAMES):
            output.write(TEMPLATE.format(**clean(row)))


xml
---
