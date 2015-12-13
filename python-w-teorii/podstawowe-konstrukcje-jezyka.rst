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
* // i **
* przypisania i porównania
* +=





.. code:: python

   operator: in
   operator: not in


Funkcje
=======

* Definiowanie funkcji
* Konwencja nazewnicza funkcji
* Funkcje wieloargumentowe
* Parametry nazwane
* Parametry z wartością domyślną
* Funkcje z operatorem * i ** w deklaracji
* operator * i ** jako parametr
* dekoratory
* closures
* introspekcja
* zwracanie wartości
* zwracanie obiektów
* value, \*args = function()
* używanie _\* \*
* lambda

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

``yield``
---------

``sorted``
----------

``range``
---------

``isinstanceof``
----------------

``__file__``
-------------

``__name__``
-------------


Funkcje wbudowane
=================

``min()``
---------

``max()``
---------

``len()``
---------

``join()``
----------

``raw_input()``
---------------

``map()``
---------

``zip()``
---------

``filter()``
------------

Print formatting
================

* stary styl
  * kolejnościowe
  * nazwane
  * typy: string, int, float
  * operatory na stringu
  * .format() - nowy styl
  * string
  * int
  * float
  * operatory na stringu
* jako parametry do print("string", \*\*args)


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

Operator ``yield``
------------------

Lazy evaluation
---------------

Iteratory
---------

Wyrażenia regularne
====================

Konstruowanie wyrażeń
---------------------

Wyciąganie parametrów (zmiennych)
---------------------------------

``match()``
----------------------------

``search()``
------------------------------

``findall()`` i ``finditer()``
------------------------------

Greedy search
-------------

Wyjątki
=======

Po co są wyjątki?
-----------------

Rodzaje wyjątków
----------------

Przechwytywanie wyjątków
------------------------
``try, catch, finally``
