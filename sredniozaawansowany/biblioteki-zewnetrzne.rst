*********************
Biblioteki zewnętrzne
*********************


Do zastosowań naukowych
=======================

``num.py``
----------

``sci.py``
----------

``pandas``
----------

``pybrain``
-----------


Wspierających programowanie sieciowe
====================================

Standard WSGI
-------------

``requests``
------------

.. code:: python

    >>> import requests

    >>> requests.put('http://httpbin.org/put', data = {'key':'value'})
    >>> requests.delete('http://httpbin.org/delete')
    >>> requests.head('http://httpbin.org/get')
    >>> requests.options('http://httpbin.org/get')

.. code:: python

    >>> payload = {'key1': 'value1', 'key2': 'value2'}
    >>> r = requests.get('http://httpbin.org/get', params=payload)
    >>> print(r.url)
    http://httpbin.org/get?key2=value2&key1=value1

    >>> payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
    >>> r = requests.get('http://httpbin.org/get', params=payload)
    >>> print(r.url)
    http://httpbin.org/get?key1=value1&key2=value2&key2=value3

.. code:: python

    >>> import requests

    >>> r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
    >>> r.status_code
    200
    >>> r.headers['content-type']
    'application/json; charset=utf8'
    >>> r.encoding
    'utf-8'
    >>> r.text
    u'{"type":"User"...'
    >>> r.json()
    {u'private_gists': 419, u'total_private_repos': 77, ...}

.. code:: python

    >>> url = 'https://api.github.com/some/endpoint'
    >>> headers = {'user-agent': 'my-app/0.0.1'}

    >>> r = requests.get(url, headers=headers)

.. code:: python

    >>> payload = {'key1': 'value1', 'key2': 'value2'}

    >>> r = requests.post("http://httpbin.org/post", data=payload)
    >>> print(r.text)
    {
      ...
      "form": {
        "key2": "value2",
        "key1": "value1"
      },
      ...
    }

.. code:: python

    >>> r = requests.head('http://github.com', allow_redirects=True)

    >>> r.url
    'https://github.com/'

    >>> r.history
    [<Response [301]>]

.. code:: python

    >>> import json

    >>> url = 'https://api.github.com/some/endpoint'
    >>> payload = {'some': 'data'}

    >>> r = requests.post(url, data=json.dumps(payload))

.. code:: python

    >>> url = 'https://api.github.com/some/endpoint'
    >>> payload = {'some': 'data'}

    >>> r = requests.post(url, json=payload)

* http://docs.python-requests.org/en/master/user/quickstart/#json-response-content
* http://docs.python-requests.org/en/master/dev/contributing/#kenneth-reitz-s-code-style


``suds``
--------

Google App Engine
=================

``django``
----------

``flask``
---------

``webapp2``
-----------

``tornado``
-----------

``atlassian-python-api``
------------------------

``fabric``
----------

``BeautifulSoup``
-----------------


Bazy danych
===========

``pyMySQL``
-----------

``psycopg2``
------------

``pymongo``
-----------

``SQLAlchemy``
--------------

Inne
====

``py2app``
----------

``docopt``
----------

``Jinja2``
----------

``pytz``
--------
