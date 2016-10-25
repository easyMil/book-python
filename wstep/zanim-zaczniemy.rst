.. _zanim-zaczniemy:

***************
Zanim zaczniemy
***************


Co to jest Python
=================

    Python - język programowania wysokiego poziomu ogólnego przeznaczenia, o rozbudowanym pakiecie bibliotek standardowych, którego ideą przewodnią jest czytelność i klarowność kodu źródłowego. Jego składnia cechuje się przejrzystością i zwięzłością.

    Python wspiera różne paradygmaty programowania: obiektowy, imperatywny oraz w mniejszym stopniu funkcyjny. Posiada w pełni dynamiczny system typów i automatyczne zarządzanie pamięcią, będąc w tym podobnym do języków Perl, Ruby, Scheme czy Tcl. Podobnie jak inne języki dynamiczne jest często używany jako język skryptowy. Interpretery Pythona są dostępne na wiele systemów operacyjnych.

    Python rozwijany jest jako projekt Open Source zarządzany przez Python Software Foundation, która jest organizacją non-profit.

Fragment pochodzi z serwisu `Wikipedia <https://pl.wikipedia.org/wiki/Python>`_.

Historia Pythona
================

    Pythona stworzył we wczesnych latach 90. Guido van Rossum - jako następcę języka ABC, stworzonego w Centrum voor Wiskunde en Informatica (CWI – Centrum Matematyki i Informatyki w Amsterdamie). Van Rossum jest głównym twórcą Pythona, choć spory wkład w jego rozwój pochodzi od innych osób. Z racji kluczowej roli, jaką van Rossum pełni przy podejmowaniu ważnych decyzji projektowych, często określa się go przydomkiem "Benevolent Dictator for Life" (BDFL).

    Nazwa języka nie pochodzi od zwierzęcia, jak można przypuszczać. Python pochodzi od serialu komediowego emitowanego w latach siedemdziesiątych przez BBC. Ten serial nosi nazwę "Monty Python's Flying Circus" (Latający Cyrk Monty Pythona). Projektant potrzebował nazwy, która była krótka, unikalna i nieco tajemnicza. Na dodatek był fanem serialu, więc uważał, że taka nazwa dla języka była świetna.

    Wersja 1.2 była ostatnią wydaną przez CWI. Od 1995 roku Van Rossum kontynuował pracę nad Pythonem w Corporation for National Research Initiatives (CNRI) w Reston w Wirginii, gdzie wydał kilka wersji Pythona, do 1.6 włącznie. W 2000 roku van Rossum i zespół pracujący nad rozwojem jądra Pythona przenieśli się do BeOpen.com by założyć zespół BeOpen PythonLabs. Pierwszą i jedyną wersją wydaną przez BeOpen.com był Python 2.0.

    Po wydaniu wersji 1.6 i opuszczeniu CNRI przez van Rossuma, który zajął się programowaniem komercyjnym, uznano za wysoce pożądane, by Pythona można było używać z oprogramowaniem dostępnym na licencji GPL. CNRI i Free Software Foundation (FSF) podjęły wspólny wysiłek w celu odpowiedniej modyfikacji licencji Pythona. Wersja 1.6.1 była zasadniczo identyczna z wersją 1.6, z wyjątkiem kilku drobnych poprawek oraz licencji, dzięki której późniejsze wersje mogły być zgodne z licencją GPL. Python 2.1 pochodzi zarówno od wersji 1.6.1, jak i 2.0.

    Po wydaniu Pythona 2.0 przez BeOpen.com Guido van Rossum i inni programiści z PythonLabs przeszli do Digital Creations. Cała własność intelektualna dodana od tego momentu, począwszy od Pythona 2.1 (wraz z wersjami alpha i beta), jest własnością Python Software Foundation (PSF), niedochodowej organizacji wzorowanej na Apache Software Foundation.

Fragment pochodzi z serwisu `Wikipedia <https://pl.wikipedia.org/wiki/Python>`_.


Którego wersję wybrać?
======================

Python kilka lat temu przeszedł drastyczną transformację. Projekt Python 3 miał całkowicie zmienić sposób w jaki kompilator traktuje kod źródłowy. Dotychczas wszystkie ciągi znaków traktowane były jako ciągi ASCII. Od teraz miało to ulec zmianie a konto popularnego na całym świecie kodowania UTF-8. Wcześniej, aby skorzystać z takiego zachowania należało przed stringiem umieścić literkę "u", np. ``u'Hello World!'`` aby kompilator zrozumiał kodowanie. Niestety nie było to domyślne kodowanie i z tego powodu konieczne było ciągłe żonglowanie funkcjami ``.encode()`` i ``.decode()``.

Ponadto w nowym języku Python 3 (czasami zwanym Python 3k [3k = 3000] aby pokazać, że drastycznie się różni od wersji 2) scalono niektóre moduły biblioteki standardowej oraz zmieniono zachowanie niektórych funkcji w tym bardzo często wykorzystywanej ``print()``, która wcześniej była słowem kluczowym w języku.

Jeżeli rozpoczynasz naukę programowania wybierz nowego Pythona 3. Jeżeli tworzysz nowy projekt wybierz podobnie. Na chwilę obecną jedynym uzasadnieniem wyboru starszej wersji jest niekompatybilność niektórych bibliotek i projektów zewnętrznych. Na szczęście z miesiąca na miesiąc lista projektów "Python 3 compliant" wzrasta i wybór pozostaje coraz bardziej oczywisty.

Ostatnią wersją gałęzi 2 jest 2.7. Wersja ta zawiera elementy i składnię ułatwiające konwersję programów do nowego środowiska i pozwala na pisanie aplikacji i skryptów, które powinny uruchomić się zarówno przy wykorzystaniu interpretera ``python2`` jak i ``python3``. Wersja 2.7 jest ostatnią z rodziny 2 i będą do niej wypuszczane jedynie poprawki bezpieczeństwa.


Który interpreter?
==================

Sam Python jest tak naprawdę tylko specyfikacją składni oraz wyglądu biblioteki standardowej. Python ma obecnie kilka interpreterów z których najbardziej popularny jest cPython, który jest wydawany razem z nową wersją specyfikacji języka.


cPython
-------

Domyślną wersją Pythona jest cPython. Jest to tzw. implementacja wzorcowa i to jej kompilator jest wydawany wraz ze specyfikacją nowych funkcjonalności przy każdym wydaniu Python. Sam kompilator jest rozwijany w języku C. cPython jest najbardziej popularną dystrybucją z wszystkich wydań. W poniższych materiałach to właśnie z tej wersji będziemy korzystać.


PyPy
----

Bardzo ciekawy projekt napisania interpretera Pythona w... Pythonie. Kompilator dokonuje bardzo wielu niskopoziomowych optymalizacji dlatego ta wersja języka jest wyjątkowo szybka. Niestety nie wszystkie biblioteki zewnętrzne są z nią kompatybilne. Nie mniej projekt jest wciąż aktywnie rozwijany przez bardzo pomysłowych programistów i stanowi solidną alternatywę dla cPythona. Niektóre programy przy wykorzystaniu PyPy potrafią przyspieszyć kilkuset do kilkutysiąc krotnie.


IronPython
----------

Próba implementacji języka Python wykorzystując platformę .NET firmy Microsoft. Dzięki temu język bardzo dobrze integruje się z całym środowiskiem.


Jython
------

Próba implementacji języka Python wykorzystując platformę wirtualnej maszyny JAVA (JVM). Projekt bardzo obiecujący lecz niestety ostatnio słabo rozwijany. JVM stanowi bardzo dobrą platformę dobrze "wygrzaną" oraz poznaną pod względem wydajnościowym jak i środowiska developerskiego.


Inne
----

W internecie jest dostępnych jeszcze więcej implementacji języka. Niektóre projekty są jeszcze rozwijane, niektóre (Stackless Python) weszły w skład lub transformowały się w wyżej wymienionych lub zostały zarzucone (Unleaden Swallow).


Instalacja
==========


Windows
-------

Aby zainstalować Python na środowisku Windows należy pobrać instalator z python.org a następnie przejść przez wszystkie kroki kreatora.
Po instalacji należy wylogować się i zalogować ponownie aby odświeżyć zmienną PATH. Po tym procesie w Windowsowej liście poleceń (cmd) będzie dostępny program ``python``.
Ponadto wraz z instalacją Pythona na Twoim komputerze zainstaluje się edytor Idle, który w początkowej fazie nauki tworzenia oprogramowania powinien nam w zupełności wystarczyć.


OS X
----

Jeżeli posiadasz OS X to Python powinien być domyślnie zainstalowany na Twoim komputerze. Apple w najnowszych systemach operacyjnych standardowo dostarcza Pythona w wersji 2.7 i 2.6. Domyślnie po wpisaniu polecenia ``python`` uruchamiany jest 2.7. Aby zainstalować Pythona w wersji 3 możemy skorzystać z managera pakietów ``brew`` albo z tzw. macports. Osobiście polecam to pierwsze podejście. Brew dostępny jest za darmo i można pobrać go z internetu uruchamiając polecenie ze strony `Brew <http://brew.sh>`_. Najpierw jednak konieczne będzie zainstalowanie najnowszej wersji Xcode z AppStore. Brew powinien zrobić to za Ciebie.

Sama instalacja brew sprowadza do uruchomienia polecenia wyglądającego jak następujące:

.. code:: bash

    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Następnie po instalacji:

.. code:: bash

    brew install python3

I już możemy cieszyć się najnowszym Pythonem.


Linux
-----

Niemalże wszystkie dystrybucje Linuxa posiadają zainstalowaną wersję Pythona w wersji 2. Aby zainstalować trójkę użyj swojego managera pakietów ``apt-get``, ``yum`` czy ``emerge`` czy ``rpm`` w zależności od dystrybucji.


Wybór IDE
=========

Do edycji skryptów Pythona wystarczy sam Notatnik. Kod źródłowy jest na tyle czytelny i prosty, że bardzo łatwo będziemy w stanie poradzić sobie z prostymi skryptami bez jakiejkolwiek pomocy od zaawansowanego edytora. Jednakże w miarę rośnięcia złożoności projektu oraz ilości plików przyda nam się coś co ułatwi nam pracę.

Wybór edytora to temat wielce kontrowersyjny. Od kilku dziesięcioleci w środowisku programistów jest prowadzona wojna między minimalistycznym VIMem oraz posiadającym ogromne możliwości EMACSem. Jeden i drugi edytor wspaniale posłuży nam do pisania skryptów w Pythonie i po odpowiedniej konfiguracji lub instalacji pluginów podpowie składnię. I choć sam jestem fanem jednego z powyższych rozwiązań (ale nie powiem którego :) to do większych projektów korzystam z czegoś zupełnie z innej beczki. Po przetestowaniu kilkunastu środowisk IDE zaprzyjaźniłem się z edytorem PyCharm. PyCharm ma dwie wersję płatną oraz darmową. Ta druga w zupełności nam wystarczy. Ciekawą alternatywą może być PyDev - plugin do środowiska Eclipse.

W poniższych materiałach będę posługiwał się kodem źródłowym, który wykonywany jest przez interpreter i nie ma znaczenia z jakiego IDE skorzystasz.


Read–Eval–Print Loop
====================

Python spopularyzował wykorzystanie tzw. interpretera REPL (read–eval–print loop). REPL to interaktywny interpreter poleceń wykonujący wyrażenia z języka (zwykle linie), których wyniki są wyświetlane użytkownikowi natychmiast po ich wykonaniu. W uproszczeniu można powiedzieć, że REPL jest to linia poleceń programu ``python``. Znakiem zachęty do wprowadzania tekstu takiego programu są trzy znaki większości ``>>>``. Polecenia wpisane po tych znaczkach są interpretowane i natychmiast wykonywane. Ich wynik przedstawiany jest w następnej linijce. Jeżeli wykorzystamy konstrukcję, która wymaga więcej niż jednej linii, każda kolejna linijka będzie poprzedzona trzema kropkami ``...``. Przykłady takiej interakcji zobaczymy przy omawianiu "Hello World".

Rozwiązanie REPL idealnie pasuje do szybkiego testowania składni oraz funkcjonalności programów i bibliotek. Dzięki REPL jesteśmy w stanie przeprowadzić interaktywną sesję z linią poleceń a po przetestowaniu rozwiązania wkleić działające linie do naszego skryptu. Taki styl znacząco przyspiesza development i debugging.

Uproszczoną implementację takiego rozwiązania można przedstawić w następujący sposób:

.. code:: python

    while True:
        command = raw_input('>>> ')
        output = eval(command)
        print(output)

W dalszej części omówimy poszczególne elementy, które są tu wymienione.


PYTHON_PATH
===========


Virtualenv
==========

Wraz z wersją Python 3.3 do języka został dodany ten genialny moduł. Aplikacja ta odpowiada na problem zarządzania zależnościami na Twojej maszynie. Dzięki użyciu Virtualenv (po włączeniu jako standard zwany ``pyvenv``. Mamy możliwość do tworzenia tzw. wirtualnych środowisk Pythona. Środowisko to zawiera w sobie plik wykonywalny języka oraz wszystkie potrzebne biblioteki wewnętrzne i zewnętrzne. Takie środowiska możemy tworzyć per projekt i nie musimy martwić się, że Projekt A wymaga np. Django w wersji 1.8 a Projekt B w 1.9.

Tworzenie takiego środowiska jest bardzo łatwe i szybkie:

.. code:: bash

    pyvenv .virtualenv
    
lub na Windowsie:

.. code:: bat

    python3 -m venv .virtualenv

I po chwili w pojawi się katalog .virtualenv ze środowiskiem. Następnie za każdym razem kiedy będziesz chciał pracować wykorzystując to środowisko będzie konieczna jego aktywacja:

.. code:: bash

    source .virtualenv/bin/activate
    
lub na Windowsie:

.. code:: bat

    .virtualenv\bin\activate.bat

Każda instalacja pakietów oraz bibliotek wykona się w środowisku. Skrypt który uruchomisz wykorzysta właśnie te wersje, które masz w nim zainstalowane.

Aby zainstalować jakieś nowe paczki należy użyć polecenia ``pip``. Od wersji Python 3.4 ``pip`` jest zainstalowany domyślnie.

.. code:: bash

    pip install pep8

Aby zobaczyć zainstalowane paczki, użyj polecenia ``pip freeze``. Przekierowując wynik tego polecenia do pliku ``requirements.txt`` stworzysz listę zależności wraz z wersjami, które są niezbędne dla uruchomienia Twojego programu.

.. code:: bash

    pip freeze > requirements.txt

Więcej na temat instalowania paczek, modularyzacji itp. znajdziesz w rozdziale tej książki poświęconym temu tematowi.


Gdzie mogę szukać ciekawych informacji
======================================

* http://www.infoq.com/python/
* http://pyvideo.org/
* https://www.jetbrains.com/pycharm/download/
* https://www.python.org - Strona do pobrania Pythona
* https://python3wos.appspot.com - Python 3 lista kompatybilnych bibliotek
