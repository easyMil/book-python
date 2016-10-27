*****************************
Podstawowe konstrukcje języka
*****************************


Stałe i Zmienne
===============

Stałe
-----

Zmienne
-------

``globals()`` i ``locals()``
----------------------------


Operatory
=========

Lista operatorów
----------------

+------------+-------------------------+
| Operacja   | Znaczenie               |
+============+=========================+
| ``<``      | mniejsze niż            |
+------------+-------------------------+
| ``<=``     | mniejsze lub równe      |
+------------+-------------------------+
| ``>``      | większe niż             |
+------------+-------------------------+
| ``>=``     | większe lub równe       |
+------------+-------------------------+
| ``==``     | równe                   |
+------------+-------------------------+
| ``!=``     | różne                   |
+------------+-------------------------+
| ``is``     | obiekty są tożsame      |
+------------+-------------------------+
| ``is not`` | obiekty nie są tożsame  |
+------------+-------------------------+

Kolejność operatorów
--------------------

* modulo
* ``//`` i ``**``
* przypisania i porównania
* ``+=``
* ``in`` i ``not in``


Podstawowe konstrukcje
======================

``if`` ... ``elif`` ... ``else``
--------------------------------

.. code:: python

    if not 0 <= k <= n:
        raise ValueError("Sample larger than population")


``not``, ``in``, ``is``
-----------------------

``switch`` statement?
---------------------

Wybitnie użyteczne pętla ``for``
--------------------------------

``while``
---------

Słowa kluczowe
==============

``pass``
--------

``continue``
------------

``break``
---------

``return``
----------

``sorted``
----------

``range``
---------

``isinstance``
----------------

``__file__``
------------

``__name__``
------------


Funkcje
=======

Definiowanie funkcji
--------------------

Konwencja nazewnicza funkcji
----------------------------

* CamelCase? Nie?! Używanie ``_`` w nazwach
* Funkcje o nazwie zaczynającej się od ``_`` przez konwencję są traktowane jako prywatne (w Pythonie nie ma private/protected/public).
* Funkcje o nazwie zaczynającej się od ``__`` i kończących się na ``__`` przez konwencję są traktowane jako systemowe.
* Nazwy opisowe funkcji

Argumenty do funkcji
--------------------

Argumenty nazwane
-----------------

Argumenty z wartością domyślną
------------------------------

Argumenty ``*args``, ``**kwargs``
---------------------------------

Korzystnie z **self.__dict__

Zwracanie wartości prostych
---------------------------

Zwracanie typów złożonych
-------------------------

Rozpakowywanie wartości zwracanych
----------------------------------

.. code:: python

    value, _ = function()
    value, *args = function()


Funkcje wbudowane
=================

``min()``
---------

``max()``
---------

``len()``
---------

``input()``
-----------


Print formatting
================

Stary styl
----------

* kolejnościowe
* nazwane
* typy: ``string``, ``int``, ``float``
* operatory na stringu

``.format()`` - nowy styl
-------------------------

* ``string``
* ``int``
* ``float``
* operatory na stringu
* jako parametry do ``print("string", **args)``

Programowanie funkcyjne
=======================

lambda
------

.. code:: python

    foo = lambda x: x*x
    print(foo(10))

    lista = [1, 2, 3, 4]
    parzyste = filter(lambda x: x % 2 == 0, lista)

closure
-------

.. code:: python

    def f(x):
        def g(y):
            return x + y
        return g

decorator
---------

* Modify arguments
* Modify returned value
* Do things before call
* Do things after call
* Avoid calling
* Modify global state
* Metadata

.. code:: python

    def my_decorator(f):
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        return wrapper

    @my_decorator
    def func(x):
        return x

.. code:: python

    func = my_decorator(f)


złożenia funkcji
----------------

``map()``
---------

.. code:: python

    x = 1
    l = [1, 2, 3]

    def f(y):
        return x + y

    map(f, l)
    map(lambda y: x + y, l)


``zip()``
---------

``filter()``
------------


Pliki
=====

Konstrukcja ``with``
--------------------

Czytanie
--------

Zapis
-----


Serializacja
============

Pickle
------

``json``
--------

xml
---


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
