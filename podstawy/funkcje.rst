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

