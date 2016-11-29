*********************
Trochę o samym języku
*********************


Wcięcia zamiast nawiasów klamrowych
===================================

Jest to chyba najbardziej ciekawa rzecz w samym języku. Autorzy specyfikacji zdecydowali się na zastąpienie nawiasów klamrowych wcięciami, czyli tzw. białymi spacjami (ang. whitespace). Jest to dość nietypowe rozwiązanie, które okazało się bardzo rewolucyjne i niesamowicie podniosło czytelność kodu źródłowego.

Sama idea spowodowała dużą polaryzację programistów. Jedni bardzo sobie chwalą to rozwiązanie, a inni przyzwyczajeni do języków przypominających składnią C są jej zaciekłymi wrogami. Osobiście jestem wielkim zwolennikiem takiego rozwiązania!

.. code:: python

    >>> from __future__ import braces
      File "<stdin>", line 1
    SyntaxError: not a chance


Końce linii
===========

Pierwszą rzeczą (poza znaczącymi wcięciami), która może zaskoczyć programistów przyzwyczajonych do składni C jest brak konieczności, a nawet zalecenie do niestawiania znaku średnika ``;`` na końcu linii. Programy interpretowane są linia po linii. Linia kończy się tam, gdzie ostatni znak polecenia.

Python pozwala na stosowanie znaków końca linii zarówno znanych z systemów Windows (\r\n) jak i środowiska \*nix (\n). W tych materiałach będziemy posługiwali się znakiem \n symbolizującym koniec linii.


Wszystko jest obiektem
======================

W Pythonie wszystkie rzeczy są obiektem. Każdy element posiada swoje metody, które możemy na nim uruchomić. W dalszej części tych materiałów będziemy korzystali z polecenia ``help()`` aby zobaczyć jakiego z jakiego typu obiektem mamy okazję pracować oraz co możemy z nim zrobić.


Duck typing
===========

W językach programowania można doszukać się wielu systemów typowania. System typowania informuje kompilator o obiekcie oraz o jego zachowaniach. Ponadto niesie za sobą informację na temat ilości pamięci, którą trzeba dla takiego obiektu zarezerwować. Istnieje nawet cała gałąź zajmująca się systemami typów. Obecnie najczęściej wykorzystywane języki programowania dzielą się na statycznie - silnie typowane (JAVA, C, C++ i pochodne) oraz dynamicznie - słabo typowane (Python, Ruby, PHP itp.). Oczywiście mogą znaleźć się rozwiązania hybrydowe oraz z tzw. inrefencją typów itp.

W naszym przypadku skupmy się na samym mechanizmie dynamicznego typowania. Określenie to oznacza, że język nie posiada typów zmiennych i obiektów, które jawnie trzeba deklarować. Inicjując zmienną nie musimy powiedzieć, że jest to ``int``. Co więcej po chwili do tej zmiennej możemy przypisać dowolny obiekt, np. łańcuch znaków i kompilator nie powie nam złego słowa. Kompilator podczas działania oprogramowania niejawnie może zmienić typ obiektu i dokonać na nim konwersji.

Wśród programistów popularne jest powiedzenie "jeżeli chodzi jak kaczka i kwacze jak kaczka, to musi być to kaczka". Od tego powiedzenia wzięła się nazwa Duck typing. Określenie to jest wykorzystywane w stosunku do języków, których typy obiektów rozpoznawane są po metodach, które można na nich wykonać. Nie zawsze takie zgadywanie jest celne i jednoznacznie i precyzyjnie określa typ. Może się okazać, że obiekt np. ``Samochód`` posiada metody ``uruchom_silnik()`` i ``jedz_prosto()`` podobnie jak ``Motor``. Jeden i drugi obiekt będzie zachowywał się podobnie. Języki wykorzystujące ten mechanizm wykorzystują specjalne metody porównawcze, które jednoznacznie dają informację kompilatorowi czy dwa obiekty są równe.

Sam mechanizm dynamicznego typowania jest dość kontrowersyjny, ze względu na możliwość bycia nieścisłym. W praktyce okazuje się, że rozwój oprogramowania wykorzystującego ten sposób jest dużo szybszy. Za to zwolennicy statycznego typowania, twierdzą, że projekty wykorzystujące duck typing są trudne w utrzymaniu po latach. Celem tego dokumentu nie jest udowadnianie wyższości jednego rozwiązania nad drugim. Zachęcam jednak do zapoznania się z wykładem "The Unreasonable Effectiveness of Dynamic Typing for Practical Programs", którego autorem jest "Robert Smallshire". Wykład zamieszczonym został w serwisie InfoQ (http://www.infoq.com/presentations/dynamic-static-typing). Wykład w ciekawy sposób dotyka problematyki porównania tych dwóch metod systemu typów. Wykład jest o tyle ciekawy, że bazuje na statystycznej analizie projektów umieszczonych na https://github.com a nie tylko bazuje na domysłach i flamewar jakie programiści lubią prowadzić.


Rozszerzenia plików Pythona
===========================

Pliki źródłowe języka Python zarówno w wersji 2 jak i 3 mają rozszerzenie ``.py``. Podczas wytwarzania oprogramowania spotkasz się jeszcze z kilkoma innymi rozszerzeniami. Mogą to być:

* ``.pyc`` - plik zawiera tzw. bytecode czyli efekt kompilacji kodu źródłowego. Python tworzy te pliki podczas kompilacji jeżeli nic nie zmienimy w naszym kodzie źródłowym, wykorzystuje je bez potrzeby analizowania i kompilowania kodu ponownie. Od wersji 3.2 pliki ``.pyc`` znajdują się w specjalnym katalogu o nazwie ``__pycache__``.

* ``.pyd`` - Windowsowy plik ze skompilowanym kodem Pythona w formie biblioteki DLL.

* ``.pyo`` - pliki zawierają obiekty wykorzystywane podczas kompilacji skryptów przy wykorzystaniu flagi -O. Są to obiekty zoptymalizowane. Od wersji 3.5 Pythona te pliki nie są już tworzone.

* ``.pyw`` - Windowsowy plik z kodem źródłowym. Takie pliki odpalane są za pomocą polecenia ``pythonw.exe``

* ``.pyx`` - Źródło cPythona, które będzie przekonwertowane do C/C++

* ``.pyz`` - Python 3.5 wprowadził możliwość tworzenia Python ZIP Archive. Takie spakowane archiwum zawiera wszystkie pliki niezbędne do uruchomienia programu. Rozszerzenie dla obiektów tego typu jest ``.pyz``. Do pakowania służy biblioteka `zipapp <https://docs.python.org/3/library/zipapp.html>`_.
