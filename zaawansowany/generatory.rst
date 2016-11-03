Generatory i list comprehension
===============================

Generatory
----------

List comprehension
------------------

* wykonywane natychmiast

.. code:: python

    [x*x for x in range(0, 30) if x % 2]

Generator expressions
---------------------

* lazy evaluation

.. code:: python

    (x*x for x in range(0, 30) if x % 2)

Operator ``yield``
------------------

Lazy evaluation
---------------

Iteratory
---------

* ``__next__()``
* ``raise StopIteration``

introspekcja
------------
