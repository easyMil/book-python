*****
Pliki
*****

Konstrukcja ``with``
====================

- Context manager

Czytanie
========

.. code:: python

    with open(FILENAME) as file:
        content = file.read()

.. code:: python

    with open(FILENAME) as file:
        content = file.readlines()

.. code:: python

    with open(FILENAME) as file:
        for line in file:
            print(line)

Zapis
=====

Tryby odczytu i zapisu
======================
