**********************
Biblioteka standardowa
**********************

``datetime``
============

.. code:: python

    import datetime

    datetime.datetime.now()
    datetime.date.today()
    datetime.datetime.now() - datetime.timedelta(hours=3)
    datetime.datetime.now().replace(tzinfo=datetime.timezone.utc)

``time``
========


``os``
======

.. code:: python

    import os

    os.path
    os.walk
    os.path.join
    os.path.abspath
    os.path.dirname

``sys``
=======

.. code:: python

    import sys

    sys.path
    sys.path.append
    sys.platform


``logging``
===========

.. code:: python

    import logging

    logging.basicConfig(level=logging.DEBUG)
    logging.basicConfig(format='[%(asctime).19s] [%(levelname)s] %(message)s')

    logging.critical('Błąd krytyczny, kończę.')
    logging.error('Błąd, ale kontynuuję.')
    logging.warning('Uwaga będę coś robił')
    logging.info('Będę coś robił')
    logging.debug('Robię to tak')


``warnings``
============

.. code:: python

    import warnings

    warnings.warn('Wersja API jest już nieaktualna', PendingDeprecationWarning)

``pprint``
==========

.. code:: python

    from pprint import pprint

    data = [
       {'first_name': 'Baked', 'last_name': 'Beans'},
       {'first_name': 'Lovely', 'last_name': 'Spam'},
       {'first_name': 'Wonderful', 'last_name': 'Spam'}
    ]

    pprint(data)

``csv``
=======

.. code:: python

    import csv

    csv.DictReader()
    csv.DictWriter()

``memoize``
===========

``json``
========

.. code:: python

    import json

    json.loads()
    json.dumps()

``sqlite``
==========

``re``
======

.. code:: python

    import re

    re.search()
    re.findall()
    re.match()
    re.compile()

``httplib``
===========

``urllib``
==========

``socket``
==========

``tempfile``
============

``io``
======

.. code:: python

    import io

    io.StringIO

``functools``
=============

``itertools``
=============

``math``
========

.. code:: python

    import math

    math.sin()
    math.cos()
    math.tan()
    math.pi

``statistics``
==============

.. code:: python

    import statistics

    statistics.avg()
    statistics.mean()
    statistics.stdev()

``random``
==========

.. code:: python

    import random

    random.sample()
    random.random()

``subprocess``
==============

.. code:: python

    import subprocess

    subprocess.Popen()

``doctest``
===========

.. code:: python

    import doctest

    doctest.testmod()


``argparse``
============

.. code::

    ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])

Define how a single command-line argument should be parsed. Each parameter has its own more detailed description below, but in short they are:

* name or flags - Either a name or a list of option strings, e.g. foo or -f, --foo.
* action - The basic type of action to be taken when this argument is encountered at the command line.
* nargs - The number of command-line arguments that should be consumed.
* const - A constant value required by some action and nargs selections.
* default - The value produced if the argument is absent from the command line.
* type - The type to which the command-line argument should be converted.
* choices - A container of the allowable values for the argument.
* required - Whether or not the command-line option may be omitted (optionals only).
* help - A brief description of what the argument does.
* metavar - A name for the argument in usage messages.
* dest - The name of the attribute to be added to the object returned by parse_args().

.. code:: python

    import argparse

    parser = argparse.ArgumentParser(
        prog='PROGRAM NAME',
        description='A foo that bars',
        epilog="And that's how you'd foo a bar")

    parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')


    parser.add_argument('--foo', nargs='?', help='foo help')
    parser.add_argument('--bar', nargs='+', help='bar help')
    parser.add_argument('--foobar', nargs='*', default=[1, 2, 3], help='BAR!')

    parser.add_argument('--integers', metavar='int', type=int, choices=range(10), nargs='+', help='an integer in the range 0..9')
    parser.add_argument('--bar', nargs='?', type=int, default=42, help='the bar to %(prog)s (default: %(default)s)')

    parser.add_argument('--move', choices=['rock', 'paper', 'scissors'])

    parser.add_argument('--length', default='10', type=int, required=True)
    parser.add_argument('--width', default=10.5, type=int, help='foo the bars before frobbling')

    parser.add_argument('--input', default='input.csv', type=argparse.FileType('r'))
    parser.add_argument('--output', default='output.c', type=argparse.FileType('w'))

    script = parser.parse_args()
