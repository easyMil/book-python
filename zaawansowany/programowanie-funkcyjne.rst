Programowanie funkcyjne
=======================

lambda
------

.. code:: python

    foo = lambda x: x*x
    print(foo(10))

    lista = [1, 2, 3, 4]
    parzyste = filter(lambda x: x % 2 == 0, lista)

closure
-------

.. code:: python

    def f(x):
        def g(y):
            return x + y
        return g

decorator
---------

* Modify arguments
* Modify returned value
* Do things before call
* Do things after call
* Avoid calling
* Modify global state
* Metadata

.. code:: python

    def my_decorator(f):
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        return wrapper

    @my_decorator
    def func(x):
        return x

.. code:: python

    func = my_decorator(f)


złożenia funkcji
----------------

``map()``
---------

.. code:: python

    x = 1
    l = [1, 2, 3]

    def f(y):
        return x + y

    map(f, l)
    map(lambda y: x + y, l)


``zip()``
---------

``filter()``
------------


