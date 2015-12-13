**********************
Wprowadzenie do języka
**********************


Hello World!
============

W lekcjach programowania utarło się, że zawsze zaczynamy od już przysłowiowego "Hello World". Skrypty czy programy tego typu nie mają na celu pokazania jak minimalną ilością znaków da się wyświetlić coś na ekranie, a sposób interakcji i przepływu programista-komputer.

W Pythonie mamy możliwość wykorzystania interpretera REPL, przykład poniżej oraz stworzenia skryptu, który wykonamy z linii poleceń.

.. code:: bash

    $ python3

    Python 3.5.1 (default, Dec  7 2015, 21:59:10)
    [GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.1.76)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.

    >>> print('Hello World!')
    Hello World!

Powyższy przykład ilustruje moment wpisania polecenia ``python``, standardowy tekst informujący o wersji i kompilacji języka oraz znak zachęty ``>>>`` (ang. prompt). Polecenia wpisujemy po tym znaku a ich wynik wyświetla się poniżej (i nie zawiera wcięcia). Dalej w materiałach będziemy posługiwali się już samym znakiem zachęty.

Drugim sposobem jest stworzenie skryptu posiadającego następujące linie. Ta metoda przydaje nam się gdy nasze programy zaczną rosnąć na więcej niż jedną dwie linijki. Warto zwrócić uwagę na pierwszą linię, na tzw. shebang ``#!`` i następujące po nim polecenie. To jest deklaracja programu, którego kod źródłowy znajduje się poniżej. Linijka ta jest opcjonalna, ale dla zachowania poprawności i warto w naszych skryptach coś takiego zadeklarować. Już po pierwszej linii widzimy, że skrypt będzie zinterpretowany jako kod źródłowy trzeciej wersji Pythona.

.. code:: bash

    #!/usr/bin/env python3

    print('Hello World!')

Wynik uruchomienia powyższego skryptu będzie identyczny z efektem uzyskanym w REPL, tzn, na naszym ekranie ukaże się napis ``Hello World``.

Dla wszystkich, którzy potrzebują wiedzieć jak wygląda najmniejszy kod, który wyświetli nam te słowa polecam poniższy kod.

.. code:: python

    print('Hello World!')


Komentarze
==========

Komentarze są wykorzystywane by podpowiedzieć programiście, który będzie czytał kod źródłowy w przyszłości co dana funkcja, metoda lub po prostu kolejna linijka kodu robi. Jestem wielkim fanem pisania tak swoich programów, aby komentarze w kodzie były zbędne. Dobrego dzielenia aplikacji na mniejsze części, właściwego stosowania whitespace'ów, precyzyjnego i opisowego ich nazywania. Komentarze mogą być bardzo przydatne, ale w większości sytuacji jeżeli potrzebujemy z nich skorzystać to znaczy, że logicznie źle rozplanowaliśmy układ naszego kodu. Ponadto komentarze mają brzydką właściwość szybkiego starzenia się, tzn. kod ewoluuje, a komentarz opisuje zachowanie starej funkcji. Może to powodować dezinformację.


Zakomentowany kod
=================

Bardzo często spotykam się z problemem zakomntowanego kodu. O ile komentarze opisujące działanie poszczególnych elementów są użyteczne to zakomentowany kod jest nieakceptowalny. Często stosujemy tą technikę by chwilowo wyłączyć działanie jakiejś funkcjonalności. Jednakże niedopuszczalne jest commitowanie zmian zawierających zakomentowany kod. Kod taki bardzo często jest już niedziałający i taki pozostanie na zawsze. Bardzo często słyszę argument, że może kiedyś będziemy chcieli powrócić do tego kodu i bez sensu będzie go wymyślać i pisać na nowo. W dobie systemów kontroli wersji sytuacja ta nie będzie stwarzała jakiegokolwiek problemu. Wystarczy przeglądnąć diffa (podgląd różnicowy) pliku albo wykonać ``git blame`` i mamy dostęp do starego sposobu.

Nieuruchamiający się i niewywoływany kod nie powinien znaleźć się w repozytorium. Kropka!


Komentowanie linii
==================

W Pythonie mamy kilka sposobów komentowania. Najprostszym z nich jest komentowanie całej linii poprzez wykorzystanie znaku zwanego "pound" lub "hash" ``#``. Ciąg znaków znajdujących się za ``#`` zostanie zignorowany przez kompilator.

.. code:: python

    >>> #na ekranie otrzymamy: Hello World!
    ... print('Hello World!')
    Hello Wold!

Tu możemy zaobserwować zachowanie, o którym wspominaliśmy trochę wcześniej, tzn. kontynuacja jest oznaczana przez znak zachęty trzech kropek ``...``.


Komentarze inline
=================

Kolejnym sposobem jest komentowanie inline tzn. w linijce. Tego typu komentarze stosuje się aby wytłumaczyć zachowanie poszczególnych linii kodu. Choć kompilator dopuszcza ich stosowanie, to w ramach dobrych praktyk lepiej zastąpić je komentarzami w linijce poprzedzającej wywołanie.

.. code:: python

    >>> print('Hello Wold!') #na ekranie otrzymamy: Hello World!
    Hello Wold!


Komentarze wieloliniowe
=======================

Komentarze wieloliniowe w Pythonie można robić na dwa sposoby poprzez wykorzystanie trzech znaków cudzysłowia:

* pojedynczego ``'''``,
* podwójnego ``"""``.

W jednym i drugim przypadku cudzysłowie podwójne lub pojedyncze będzie oznaczało początek jak i koniec komentarza. Rodzaj cudzysłowiów nie ma znaczenia, ale utarło się aby stosować podwójne ``"``. W materiałach będziemy korzystać właśnie z tej notacji.

.. code:: python

    """
    Tu jest treść komentarza, który obejmuje wiele linii
    W ramach dobrych praktyk, powinniśmy takim komentarzem opisać każdą z funkcji,
    aby narzędzia takie jak np. ``help()`` wyświetlały ładne podpowiadanie działania.
    """

Są dwie szkoły tworzenia takich komentarzy. Jedna mówi, aby tekst pisać bezpośrednio po znaku cudzysłowia, a druga od nowej linijki. Jest to kwestia estetyki i czytelności komentarza.


Deklaracja interpretera
=======================

Jest to specjalny rodzaj komentarza który opisaliśmy pokrótce powyżej. Ten typ komentarza występuje tylko w pierwszej linii programu i definiuje interpreter kodu źródłowego dla kodu poniżej.

.. code:: bash

    #!/usr/bin/env python3


Deklaracja kodowania znaków w pliku
===================================

Jest to kolejny rodzaj specjalnego komentarza, który instruuje interpreter i jawnie wskazuje na sposób kodowania znaków w pliku z kodem źródłowym. W skryptach Pythona w wersji drugiej był obowiązkowy, jeżeli w kodzie lub komentarzach w pliku znajdowały się znaki z poza zakresu ASCII, np. polskie znaki diakrytyczne ą, ę, ś, ć itp.

.. code:: python

    # -*- coding: utf-8 -*-


Informacja na temat modułu
==========================

Pierwszy wielolinijkowy komentarz w pliku jest traktowany jako opis modułu. Może się w nim znajdować np. licencja użytkowania programu, instrukcja jego obsługi itp. Bardzo ciekawym pomysłem jest również napisanie komentarza opisującego parametry programów wykorzystującego standard \*unix takiego opisu. Dzięki temu poza samym jednoznacznym opisem działania programu zgodnym z ogólnie przyjętą konwencją dostajemy możliwość wykorzystania modułu docopt do jego sparsowania i obsługi parametrów przekazywanych z linii poleceń.

Docopt bierze opis z komentarza i parsuje zmienne zgodnie z instrukcją czyniąc niektóre elementy obligatoryjnymi, możliwymi do podania jedno- lub wielokrotnie itp. Samym opisem działania tego modułu zajmiemy się w sekcji jemu poświęconej.


Doctesty
========

Ostatnim niezwykle użytecznym sposobem komentowania są tzw. doctesty. W wielolinijkowym komentarzu wpisujemy sesję z interpreterem a po uruchomieniu doctestów otrzymujemy informację czy nasza funkcja poprawnie się wykonuje. Jest to bardzo proste narzędzie, które poza samym pokazaniem jak działa funkcja, jakie parametry przyjmuje i co zwraca daje możliwość weryfikacji poprawności działania kodu. W tych materiałach nieraz będziemy korzystać z tego rozwiązania.

.. code:: python

    def sumowanie_liczb(a, b):
        """Funkcja sumuje dwie liczby podane jako argumenty:

        >>> sumowanie_liczb(1, 2)
        3
        >>> sumowanie_liczb(-1, 1)
        0
        >>> sumowanie_liczb(0, 0)
        0
        """
        return a + b

Wykorzystując taki zapis natychmiast widzimy co dzieje się w danym rozwiązaniu. Doctesty bardzo przydają się przede wszystkim do zastosowań wykorzystujących wyrażenia regularne, których zrozumienie zapisu często wymaga chwili zastanowienia.
