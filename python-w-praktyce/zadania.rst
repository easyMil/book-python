*******
Zadania
*******

REST API
========

Używając biblioteki standardowej w Pythonie zaciągnij informacje o repozytoriach użytkownika MattAgile na Github.com

* https://api.github.com/users/MattAgile/repos
* Następnie z przeglądnij listę z poziomu Pythona i znajdź URL dla repozytorium ``workshop-python``.
* Przeglądnij to repozytorium i jego listę commitów.
* Podaj datę i opis ostatniego commita
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

