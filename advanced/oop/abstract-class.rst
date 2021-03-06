****************
Abstract Classes
****************


Rationale
=========
* Cannot instantiate
* Possible to indicate which method must be implemented by child
* Inheriting class must implement all methods
* Some methods can have implementation

.. glossary::
    abstract class
        Class which can only be inherited, not instanciated

    abstract method
        Method must be implemented in a subclass

    abstract static method
        Static method which must be implemented in a subclass


Syntax
======
.. code-block:: python

    from abc import ABC, abstractmethod


    class Astronaut(ABC):

        @abstractmethod
        def hello(self):
            pass


    astro = Astronaut()
    # TypeError: Can't instantiate abstract class Astronaut with abstract methods hello

.. code-block:: python

    from abc import ABCMeta, abstractmethod


    class Astronaut(metaclass=ABCMeta):

        @abstractmethod
        def hello(self):
            pass


    astro = Astronaut()
    # TypeError: Can't instantiate abstract class Astronaut with abstract methods hello


Errors
======
.. code-block:: python
    :caption: In order to use Abstract Base Class you must create abstract method. Otherwise it won't prevent from instantiating.

    from abc import ABC

    class Astronaut(ABC):
        pass

    astro = Astronaut()
    print('ok')
    # ok

.. code-block:: python
    :caption: Must implement all abstract methods

    from abc import ABC, abstractmethod

    class Human(ABC):
        @abstractmethod
        def get_name(self):
            pass

    class Asrtronaut(Human):
        pass


    astro = Asrtronaut()
    # TypeError: Can't instantiate abstract class Asrtronaut with abstract methods get_name

.. code-block:: python
    :caption: ``abc`` is common name and it is very easy to create file, variable lub module with the same name as the library, hence overwrite it. In case of error. Check all entries in ``sys.path`` or ``sys.modules['abc']`` to find what is overwriting it.

    from pprint import pprint
    import sys


    sys.modules['abc']
    # <module 'abc' from '/usr/local/Cellar/python@3.8/3.8.3/Frameworks/Python.framework/Versions/3.8/lib/python3.8/abc.py'>

    pprint(sys.path)
    # ['/Users/matt/Developer/book-python/advanced/oop/solution',
    #   '/Users/matt/Developer/pythonadv-capgemini/MattH',
    #   '/Applications/PyCharm 2020.2 EAP.app/Contents/plugins/python/helpers/pydev',
    #   '/Users/matt/Developer/pythonadv-capgemini',
    #   '/Users/matt/Developer/book-python',
    #   '/Users/matt/Developer/pythonadv-capgemini/MattH',
    #   '/Users/matt/Developer/book-python/_tmp',
    #   '/Applications/PyCharm 2020.2 '
    #   'EAP.app/Contents/plugins/python/helpers/pycharm_display',
    #   '/Applications/PyCharm 2020.2 '
    #   'EAP.app/Contents/plugins/python/helpers/third_party/thriftpy',
    #   '/Applications/PyCharm 2020.2 EAP.app/Contents/plugins/python/helpers/pydev',
    #   '/usr/local/Cellar/python@3.8/3.8.3/Frameworks/Python.framework/Versions/3.8/lib/python38.zip',
    #   '/usr/local/Cellar/python@3.8/3.8.3/Frameworks/Python.framework/Versions/3.8/lib/python3.8',
    #   '/usr/local/Cellar/python@3.8/3.8.3/Frameworks/Python.framework/Versions/3.8/lib/python3.8/lib-dynload',
    #   '/Users/matt/Developer/book-python/.venv-3.8.3/lib/python3.8/site-packages',
    #   '/Applications/PyCharm 2020.2 '
    #   'EAP.app/Contents/plugins/python/helpers/pycharm_matplotlib_backend',
    #   '/Users/matt/Developer/book-python',
    #   '/Users/matt/Developer/book-python/_tmp']


Examples
========
.. code-block:: python
    :caption: Abstract Class

    from abc import ABC, abstractmethod


    class Document(ABC):
        def __init__(self, filename):
            self.filename = filename
            self.content = self._read_file_content(filename)

        def _read_file_content(self):
            with open(self.filename, mode='rb') as file:
                return file.read()

        @abstractmethod
        def display(self):
            pass


    class PDFDocument(Document):
        def display(self):
            # display "self.content" as PDF Document

    class WordDocument(Document):
        def display(self):
            # display "self.content" as Word Document


    file1 = PDFDocument('filename.pdf')
    file1.display()

    file2 = Document('filename.txt')  # TypeError: Can't instantiate abstract class Document with abstract methods display


Assignments
===========

OOP Abstract Iris
-----------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/oop_abstract_iris.py`

:English:
    #. Create abstract class ``Iris``
    #. Create abstract method ``get_name()`` in ``Iris``
    #. Create class ``Setosa`` inheriting from ``Iris``
    #. Try to create instance of a class ``Setosa``
    #. Try to create instance of a class ``Iris``

:Polish:
    #. Stwórz klasę abstrakcyjną ``Iris``
    #. Stwórz metodę abstrakcyjną ``get_name()`` w ``Iris``
    #. Stwórz klasę ``Setosa`` dziedziczące po ``Iris``
    #. Spróbuj stworzyć instancje klasy ``Setosa``
    #. Spróbuj stworzyć instancję klasy ``Iris``
