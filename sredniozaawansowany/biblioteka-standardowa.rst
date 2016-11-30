**********************
Biblioteka standardowa
**********************

``datetime``
============

.. code:: python

    >>> import datetime
    >>> datetime.datetime.now()
    >>> datetime.date.today()
    >>> datetime.datetime.now() - datetime.timedelta(hours=3)
    >>> datetime.datetime.now().replace(tzinfo=datetime.timezone.utc)

``time``
========


``os``
======

.. code:: python

    >>> os.path
    >>> os.walk
    >>> os.path.join
    >>> os.path.abspath
    >>> os.path.dirname

``sys``
=======

.. code:: python

    >>> import sys
    >>> sys.path
    >>> sys.path.append
    >>> sys.platform

``abc``
=======

``@abc.abstractmethod``
-----------------------

``logging``
===========

.. code:: python

    >>> import logging
    >>> logging.basicConfig(level=logging.DEBUG)
    >>> logging.basicConfig(format='[%(asctime).19s] [%(levelname)s] %(message)s')
    >>> logging.critical('Błąd krytyczny, kończę.')
    >>> logging.error('Błąd, ale kontynuuję.')
    >>> logging.warning('Uwaga będę coś robił')
    >>> logging.info('Będę coś robił')
    >>> logging.debug('Robię to tak')


``warnings``
============

.. code:: python

    >>> import warnings
    >>> warnings.warn('Wersja API jest już nieaktualna', PendingDeprecationWarning)

``pprint``
==========

``csv``
=======

.. code:: python

    >>> csv.DictReader()
    >>> csv.DictWriter()

``memoize``
===========

``json``
========

.. code:: python

    >>> json.loads()
    >>> json.dumps()

``sqlite``
==========

``re``
======

.. code:: python

    >>> re.search()
    >>> re.findall()
    >>> re.match()
    >>> re.compile()

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

    >>> io.StringIO

``functools``
=============

``itertools``
=============

``math``
========

.. code:: python

    >>> math.sin()
    >>> math.cos()
    >>> math.tan()
    >>> math.pi

``statistics``
==============

.. code:: python

    >>> statistics.avg()
    >>> statistics.mean()
    >>> statistics.stdev()

``random``
==========

.. code:: python

    >>> random.sample()
    >>> random.random()

``subprocess``
==============

.. code:: python

    >>> subprocess.Popen()

``doctest``
===========

.. code:: python

    >>> import doctest
    >>> doctest.testmod()


``argparse``
============

.. code:: python

    >>> parser = argparse.ArgumentParser()
    >>> parser.add_argument('--input', default='input.csv', type=argparse.FileType('r'))
    >>> parser.add_argument('--output', default='output.c', type=argparse.FileType('w'))
    >>> script = parser.parse_args()
