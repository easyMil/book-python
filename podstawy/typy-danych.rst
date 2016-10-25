***********
Typy danych
***********

Numeryczne typy danych
======================

``int`` - Liczba całkowita
--------------------------

Jednym z najbardziej podstawowych typów danych jest ``int``.
``int()`` jest funkcją wbudowaną, która zamieni swój argument na liczbę całkowitą.


``float`` - Liczba zmiennoprzecinkowa
-------------------------------------

``float`` w Pythonie reprezentuje liczbę zmiennoprzecinkową. Ciekawą własnością tego typu jest możliwość reprezentacji nieskończoności za pomocą ``Infinity`` oraz minus nieskończoności ``-Infinity``. Więcej szczegółów dostępnych jest w dokumentacji dla tego `typu <https://docs.python.org/3/library/functions.html#grammar-token-infinity>`_

Podobnie jak pozostałe typy ``float()`` jest funkcją, która konwertuje swój argument na liczbę zmiennoprzecinkową.

.. code:: python

    >>> float('+1.23')
    1.23
    >>> float('   -12345\n')
    -12345.0
    >>> float('1e-003')
    0.001
    >>> float('+1E6')
    1000000.0
    >>> float('-Infinity')
    -inf


``complex`` - liczba zespolona
------------------------------

``complex`` reprezentuje typ liczby zespolonej posiadającej część rzeczywistą oraz urojoną. Należy zwrócić uwagę, że argument powinien być ciągiem znaków niezawierającym spacji. W przeciwnym przypadku otrzymamy ``ValueError``.

.. code:: python

    >>> complex('1+2j')
    (1+2j)
    >>> complex('1 + 2j')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: complex() arg is a malformed string


Operacje na typach numerycznych
-------------------------------

+---------------------+---------------------------------+
| Operacja            | Rezultat                        |
+=====================+=================================+
| ``x + y``           | suma *x* i *y*                  |
+---------------------+---------------------------------+
| ``x - y``           | różnica *x* i *y*               |
+---------------------+---------------------------------+
| ``x * y``           | iloczyn *x* i *y*               |
+---------------------+---------------------------------+
| ``x / y``           | iloraz *x* i *y*                |
+---------------------+---------------------------------+
| ``x // y``          | podłoga z ilorazu *x* i *y*     |
+---------------------+---------------------------------+
| ``x % y``           | reszta z dzielenia ``x / y``    |
+---------------------+---------------------------------+
| ``-x``              | *x* negacja                     |
+---------------------+---------------------------------+
| ``+x``              | *x* bez zmiany                  |
+---------------------+---------------------------------+
| ``abs(x)``          | wartość bezwzględna *x*         |
+---------------------+---------------------------------+
| ``int(x)``          | *x* przekonwertowane do int     |
+---------------------+---------------------------------+
| ``float(x)``        | *x* przekonwertowane do float   |
+---------------------+---------------------------------+
| ``complex(re, im)`` | liczba zespolona:               |
|                     | *re* - część rzeczywista        |
|                     | *im* - część urojona            |
+---------------------+---------------------------------+
| ``divmod(x, y)``    | para ``(x // y, x % y)``        |
+---------------------+---------------------------------+
| ``pow(x, y)``       | *x* podniesione do potęgi *y*   |
+---------------------+---------------------------------+
| ``x ** y``          | *x* do potęgi *y*               |
+---------------------+---------------------------------+

Tekstowe typy danych
====================

``str`` - Ciąg znaków
---------------------

Obiekt typu ``str`` przechowuje łańcuch znaków. ``str()`` jest także funkcją, która zwraca ciąg znaków z argumentu.

Niemutowalność
--------------

Ważną cechą ciągów znakowych jest tzw. niemutowalność. Gdy wykonujemy operację na stringu tworzona jest jego nowa kopia.


Różnica między ' a "
--------------------

Python nie rozróżnia czy stosujemy pojedyncze znaki cudzysłowiu czy podwójne.
Ważne jest aby wybrać jedną konwencję i się jej konsekwentnie trzymać.

Interpreter Pythona domyślnie stosuje pojedyncze znaki cudzysłowia, z tego powodu w tym materiale będziemy trzymać się tej konwencji.

Operacje na stringach
---------------------

* ``strip()``, ``lstrip()``, ``rstrip()``
* ``join()``
* ``startswith()``
* ``title()``
* ``replace()``
* Wycinanie części stringów

Konwersja stringów
------------------

* ``bin()``
* ``hex()``
* ``oct()``

Logiczne typy danych
====================

``bool`` - Wartość logiczna
---------------------------

Obiekt typu ``bool`` może przyjąć dwie wartości logiczne:

* True
* False

Zwróć uwagę na wielkość liter!

``bool()`` to także funkcja wbudowana w język Python, która zwraca wartość logiczną wyrażenia.

``None`` - Wartość pusta
------------------------

Złożone typy danych
===================

``tuple`` - Krotka
------------------

``list`` - Lista
----------------

``set`` - Zbiór
---------------

``dict`` - Słownik
------------------

Dobieranie się do wartości elementów
------------------------------------

``[0]`` i ``.get(0)``
---------------------

Rozszerzone typy danych
=======================

Lista słowników
---------------

Listy wielowymiarowe
--------------------

Drzewa
------

Jak inicjować poszczególne typy?
================================
