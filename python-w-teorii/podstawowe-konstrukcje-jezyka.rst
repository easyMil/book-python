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

``isinstanceof``
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
* Funkcje o nazwie zaczynającej się od ``_``
* Nazwy opisowe funkcji

Argumenty do funkcji
--------------------

Argumenty nazwane
-----------------

Argumenty z wartością domyślną
------------------------------

Argumenty ``*args``, ``**kwargs``
---------------------------------

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


Generatory i list comprahention
===============================

Generatory
----------

List comprahention
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

Wyrażenia regularne
===================

Konstruowanie wyrażeń
---------------------

Wyciąganie parametrów (zmiennych)
---------------------------------

``match()``
-----------

``search()``
------------

``findall()`` i ``finditer()``
------------------------------

Greedy search
-------------

Wyjątki
=======

Po co są wyjątki?
-----------------

Najpopularniejsze wyjątki
-------------------------

+---------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Nazwa wyjątku       | Opis                                                                                                                                                                                                                                                                                                |
+=====================+=====================================================================================================================================================================================================================================================================================================+
| AttributeError      | Raised when an attribute reference (see Attribute references) or assignment fails. (When an object does not support attribute references or attribute assignments at all, TypeError is raised.)                                                                                                     |
+---------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ImportError         | Raised when an import statement fails to find the module definition or when a from ... import fails to find a name that is to be imported.                                                                                                                                                          |
+---------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| IndexError          | Raised when a sequence subscript is out of range. (Slice indices are silently truncated to fall in the allowed range; if an index is not an integer, TypeError is raised.)                                                                                                                          |
+---------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| KeyError            | Raised when a mapping (dictionary) key is not found in the set of existing keys.                                                                                                                                                                                                                    |
+---------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| KeyboardInterrupt   | Raised when the user hits the interrupt key (normally Control-C or Delete). During execution, a check for interrupts is made regularly. The exception inherits from BaseException so as to not be accidentally caught by code that catches Exception and thus prevent the interpreter from exiting. |
+---------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| NameError           | Raised when a local or global name is not found. This applies only to unqualified names. The associated value is an error message that includes the name that could not be found.                                                                                                                   |
+---------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| NotImplementedError | This exception is derived from RuntimeError. In user defined base classes, abstract methods should raise this exception when they require derived classes to override the method.                                                                                                                   |
+---------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| RuntimeError        | Raised when an error is detected that doesn’t fall in any of the other categories. The associated value is a string indicating what precisely went wrong.                                                                                                                                           |
+---------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SyntaxError         | Raised when the parser encounters a syntax error. This may occur in an import statement, in a call to the built-in functions exec() or eval(), or when reading the initial script or standard input (also interactively).                                                                           |
+---------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| IndentationError    | Base class for syntax errors related to incorrect indentation. This is a subclass of SyntaxError.                                                                                                                                                                                                   |
+---------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| TypeError           | Raised when an operation or function is applied to an object of inappropriate type. The associated value is a string giving details about the type mismatch.                                                                                                                                        |
+---------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Przechwytywanie wyjątków
------------------------

* ``try``
* ``catch``
* ``finally``

Hierarchia wyjątków
-------------------

.. code::

    BaseException
     +-- SystemExit
     +-- KeyboardInterrupt
     +-- GeneratorExit
     +-- Exception
          +-- StopIteration
          +-- StopAsyncIteration
          +-- ArithmeticError
          |    +-- FloatingPointError
          |    +-- OverflowError
          |    +-- ZeroDivisionError
          +-- AssertionError
          +-- AttributeError
          +-- BufferError
          +-- EOFError
          +-- ImportError
          +-- LookupError
          |    +-- IndexError
          |    +-- KeyError
          +-- MemoryError
          +-- NameError
          |    +-- UnboundLocalError
          +-- OSError
          |    +-- BlockingIOError
          |    +-- ChildProcessError
          |    +-- ConnectionError
          |    |    +-- BrokenPipeError
          |    |    +-- ConnectionAbortedError
          |    |    +-- ConnectionRefusedError
          |    |    +-- ConnectionResetError
          |    +-- FileExistsError
          |    +-- FileNotFoundError
          |    +-- InterruptedError
          |    +-- IsADirectoryError
          |    +-- NotADirectoryError
          |    +-- PermissionError
          |    +-- ProcessLookupError
          |    +-- TimeoutError
          +-- ReferenceError
          +-- RuntimeError
          |    +-- NotImplementedError
          |    +-- RecursionError
          +-- SyntaxError
          |    +-- IndentationError
          |         +-- TabError
          +-- SystemError
          +-- TypeError
          +-- ValueError
          |    +-- UnicodeError
          |         +-- UnicodeDecodeError
          |         +-- UnicodeEncodeError
          |         +-- UnicodeTranslateError
          +-- Warning
               +-- DeprecationWarning
               +-- PendingDeprecationWarning
               +-- RuntimeWarning
               +-- SyntaxWarning
               +-- UserWarning
               +-- FutureWarning
               +-- ImportWarning
               +-- UnicodeWarning
               +-- BytesWarning
               +-- ResourceWarning
