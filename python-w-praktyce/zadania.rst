*******
Zadania
*******

REST API
========

Używając biblioteki standardowej w Pythonie zaciągnij informacje o repozytoriach użytkownika Django na https://github.com

* https://github.com/django/django/commits/master
* Następnie z przeglądnij listę z poziomu Pythona i znajdź URL dla repozytorium ``django``.
* Przeglądnij to repozytorium i jego listę commitów.
* Podaj datę i opis ostatniego commita
* Znajdź numery ID ticketów (``Fixed #...``) z issue trackera, które zostały rozwiązane w ostatnim miesiącu
* Spróbuj skorzystać zamiast biblioteki standardowej z pakietu ``requests``

Generatory vs. Przetwarzanie Listy
==================================

Napisz program, który wczyta plik ``/etc/passwd``, a następnie:

* przefiltruje linie, tak aby nie zawierały komentarzy (zaczynające się od ``#``)
* przefiltruje linie, aby wyciągnąć konta systemowe - użytkowników, którzy mają UID (trzecie pole) mniejsze niż 1000
* zwróci listę loginów takich użytkowników

* Zaimplementuj rozwiązanie wykorzystując zwykłą funkcję.
* Zaimplementuj rozwiązanie wykorzystując generator i słówko kluczowe ``yield``.

* Porównaj wyniki jednego i drugiego rozwiązania przez użycie ``sys.getsizeof()``

Mini Botnet
===========

Stwórz program, który otworzy socket na porcie na localhoście podanym przez użytkownika z linii poleceń (wykorzystaj ``argparse``) i będzie nasłuchiwał połączeń. Zweryfikuj za pomocą ``telnet`` albo ``netcat`` czy program odpowiada. Następnie napisz w pythonie klienta, który będzie wysyłał polecenia do tamtego programu.

Uwaga, nigdy nie rób tego na produkcji bez tzw. sanityzacji parametrów, np. lista zaufanych hostów, możliwe polecenia!

* zrób aby przetwarzanie requestów było nieblokujące, tzn. otwieraj wątek dla każdego zapytania
* program wykona polecenie za pomocą ``eval``, które przyszło z zapytania
* wykonaj polecenie za pomocą Subproces i Popen w systemie operacyjnym i zwróć klientowi odpowiedź
* dodaj funkcję aby wyświetlał dowolny plik ``cat SCIEZKA/NAZWA`` (użyj ``os.path.join`` do łączenia sciezki i nazwy pliku
* dodaj funkcję aby listował dowolny katalog - wykorzystaj ``os.walk`` oraz ``os.path.join`` do łączenia nazw katalogów
* zmodyfikuj program aby przyjmował zapytania w formacie XML, pole command oraz arguments powinny być osobno
* zmodyfikuj program aby przyjmował zapytania w formacie JSON, pole command oraz arguments powinny być osobno
* stwórz dekorator ``localhost_only``, który będzie sprawdzał IP źródłowe połączenia i jeżeli nie pochodzi z ``127.0.0.1`` odmówi wykonania polecenia
* stwórz dekorator ``log_request``, który weźmie parametry zapytania (IP, polecenie, argumenty) i zapisze je do pliku ``/tmp/botnet.log`` w formacie ``Request from IP:PORT to execute COMMAND ARGUMENTS``

