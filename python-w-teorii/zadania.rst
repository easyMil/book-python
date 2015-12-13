*******
Zadania
*******

Powielanie napisów
==================

:Nazwa skryptu: ``bin/powielanie-napisow.py``
:Uruchamianie: ``python bin/powielanie-napisow.py``

Napisz program, który wczyta od użytkownika pewien napis, a następnie wyświetli 30 kopii tego napisu, każda w osobnej linii.

Napisz trzy wersje tego programu:

* wykorzystując ``range()``
* wykorzystując pętlę while
* wykorzystując właściwości mnożenia stringów


Napisz doctest do takiej funkcji.


Sprawdzanie danych użytkownika
==============================

Parzystość
----------

:Nazwa skryptu: ``bin/parzystosc.py``
:Uruchamianie: ``python bin/parzystosc.py``

Napisz program, który wczyta od użytkownika liczbę całkowitą i wyświetli informację, czy jest to liczba parzysta, czy nieparzysta.

Liczby całkowite
----------------

:Nazwa skryptu: ``bin/calkowite.py``
:Uruchamianie: ``python bin/calkowite.py``

Napisz program, który wczyta od użytkownika liczbę i wyświetli informację, czy jest to liczba całkowita, czy niecałkowita.


Dzienniczek ucznia
==================

:Nazwa skryptu: ``bin/oceny.py``
:Uruchamianie: ``python bin/oceny.py``

Napisz program, który wczytuje od użytkownika kolejne oceny i:

* sprawdza czy wprowadzona ocena jest na liście dopuszczalnych na wydziale ocen
* jeżeli ocena jest na liście dopuszczalnych na wydziale ocen, dodaje ją na listę otrzymanych ocen
* jeżeli wciśnięto sam Enter, oznacza to koniec listy otrzymanych ocen
* wyświetla wyliczoną dla listy otrzymanych ocen średnią arytmetyczną.


Przeliczenia trygonometryczne
=============================

:Nazwa skryptu: ``bin/trygonometria.py``
:Uruchamianie: ``python bin/trygonometria.py``

Napisz program, który wczyta od użytkownika wielkość kąta w stopniach i wyświetli wartość czterech podstawowych funkcji trygonometrycznych (sin, cos, tg, ctg) o ile dla danego kąta jest to możliwe.


Wyrazy
======

:Nazwa skryptu: ``bin/podzial-wyrazow.py``
:Uruchamianie: ``python bin/podzial-wyrazow.py``

Napisz program, który wczyta od użytkownika pewien tekst, a następnie podzieli go na zdania (zakładamy, że jednoznacznie kropka rozdziela zdania) i dla każdego zdania wyświetli ile jest w nim wyrazów (zakładamy, że spacja oddziela wyrazy w zdaniu).


Lotto
=====

:Nazwa skryptu: ``bin/lotto.py``
:Uruchamianie: ``python bin/lotto.py``

Napisz program, który wyświetli 6 losowych i nie powtarzających się liczb z zakresu od 1 do 49.


Przeliczanie temperatury
========================

:Nazwa skryptu: ``bin/temperatura.py``
:Uruchamianie: ``python bin/temperatura.py``

Woda zamarza przy 32 stopniach Fahrenheita, a wrze przy 212 stopniach Fahrenheita. Napisz program, który wyświetli tabelę przeliczeń stopni Celsjusza na stopnie Fahrenheita w zakresie od –20 do +40 stopni Celsjusza (co 5 stopni). Pamiętaj o wyświetlaniu znaku plus/minus przy temperaturze.

* Fahrenheit to Celsius: (°F - 32) / 1.8 = °C
* Celsius to Fahrenheit: (°C * 1.8) + 32 = °F

Oczywiście napisz testy do rozwiązania


Zbalansowanie nawiasów
======================

:Nazwa skryptu: ``bin/zbalansowanie-nawiasow.py``
:Uruchamianie: ``python bin/zbalansowanie-nawiasow.py``

Napisz kod który sprawdzi zbalansowanie nawiasów, tzn. czy ilość otwieranych nawiasów jest równa ilości nawiasów zamykanych. Zwórć uwagę, że mogą być cztery typy nawiasów:

* okrągłe: ``(`` i ``)``
* kwadratowe: ``[`` i ``]``
* klamrowe ``{`` i ``}``
* trójkątne ``<`` i ``>``

Rozbuduj poniższy zestaw testów i napisz funkcjonalność.

.. code:: python

    >>> dane = "() [] () ([]()[])"
    >>> zbalansowanie_nawiasow(a)
    True
    >>> dane = "( (] ([)]"
    >>> zbalansowanie_nawiasow(a)
    False

Zadanie z gwiazdką
------------------

Spróbuj użyć rekurencji.


Pole trójkąta
=============

:Nazwa skryptu: ``bin/pole-trojkata.py``
:Uruchamianie: ``python bin/pole-trojkata.py``

Napisz program, który obliczy pole trójkąta, pod warunkiem że użytkownik poda wysokość i długość podstawy tego trójkąta. Uwzględnij, że wysokość i długość podstawy mogą być liczbami niecałkowitymi.
Wykorzystaj doctest do przetestowania funckji.


Wyliczanie średniej dla parametrów
==================================

Wersja prosta
-------------

:Nazwa skryptu: ``bin/srednia.py``
:Uruchamianie: ``python bin/srednia.py``

Zdefiniuj funkcję "avg", która dla dowolnej liczby parametrów zwróci ich średnią arytmetyczną (lub 0 dla 0 parametrów).

Wersja trudniejsza
------------------

:Nazwa skryptu: ``bin/srednia.py``
:Uruchamianie: ``python bin/srednia.py`` 5 10 100 32 -90 27.5

Dowolna liczba parametrów podanych z linii poleceń


Konwersja liczby na zapis słowny
================================

:Nazwa skryptu: ``bin/konwersja-liczby.py``
:Uruchamianie: ``python bin/konwersja-liczby.py``

Wersja prosta
-------------

Napisz program "numer.py``", który zamieni wprowadzony przez użytkownika ciąg cyfr na formę tekstową:

* znaki nie będące cyframi mają być ignorowane
* konwertujemy cyfry, nie liczby, a zatem:
  * 911 to "dziewięć jeden jeden"
  * 1100 to "jeden jeden zero zero"

Wersja trudniejsza
------------------

Napisz program, który przekonwertuje liczbę na zapis słowny, np.:

.. code:: python

    >>> int_to_str(999)
    'dziewiećset dziewięćdziesiąt dziewięć'
    >>> int_to_str(127.32)
    'sto dwadzieścia siedem i trzydzieści dwa setne'

Zakres:

* 6 cyfr przed przecinkiem
* 5 cyft po przecinku

Napisz testy sprawdzające przypadki brzegowe.


Rzymskie
========

:Nazwa skryptu: ``bin/rzymskie.py``
:Uruchamianie: ``python bin/rzymskie.py``

Napisz program, który przeliczy wprowadzoną liczbę rzymską na jej postać dziesiętną.

Zrób drugą funkcję, która dokona procesu odwrotnego.

``map()``, ``filter()`` i ``lambda``
====================================

:Nazwa skryptu: ``bin/funkcyjne.py``
:Uruchamianie: ``python bin/funkcyjne.py``

Używając generatora zbuduj listę zawierającą wszystkie liczby podzielne przez 3 z zakresu od 1 do 33.

Następnie:
* Używając funkcji filter usuń z niej wszystkie liczby parzyste
* Używając wyrażenia lambda i funkcji map podnieś wszystkie elementy tak otrzymanej listy do sześcianu
* Odpowiednio używając funkcji reduce i len oblicz średnią arytmetyczną z elementów tak otrzymanej listy.


Zawartość pliku
===============

:Nazwa skryptu: ``bin/zawartosc-pliku.py``
:Uruchamianie: ``python bin/zawartosc-pliku.py``

Napisz program, który wyświetli na ekranie zawartość pliku o nazwie podanej przez użytkownika.


Książka adresowa
================

:Nazwa skryptu: ``bin/ksiazka-adresowa.py``
:Uruchamianie: ``python bin/ksiazka-adresowa.py``

Typy proste
-----------

Napisz książkę adresową, która będzie zapisywała dane do pliku w formacie json.
Każdy z użytkowników jest reprezentowany przez:

* imię
* nazwisko
* telefon
* adres

 * ulica
 * miasto
 * kod_pocztowy
 * wojewodztwo
 * panstwo

Wszystkie dane w książce muszą być reprezentowane przez typy proste.

CSV
---

Bardzo często wykorzystywanym typem pliku jest CSV, czyli wartości oddzielone przecinkami. Zamień format pliku na ten typ. Zrób tak, aby dane trafiły do odpowiednich kolumn nawet po przesortowaniu.

Klasy
-----

Zmodyfikuj program aby wykorzystywał klasy do reprezentowania wpisów w książce.
Które podejście jest lepsze?

Baza danych
-----------

Teraz wykorzystaj plik bazy danych sqlite aby trzymać informacje w tabeli.
Które podejście jest lepsze?

Django
------

Wykorzystaj Django do stworzenia takiego modelu i wygeneruj panel administracyjny.
Trudne?

Disclaimer
==========

Część zadań pochodzi z http://astronomia.zagan.pl/pliki/python/Podrecznik_Pythona.pdf
