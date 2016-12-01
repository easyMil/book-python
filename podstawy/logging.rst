*****************
Logowanie zdarzeń
*****************

Poziomy logowania
=================

* Critical
* Error
* Warning
* Info
* Debug

Korzystanie z ``logging``
=========================

.. code-block:: python

    logging.critical('Błąd krytyczny, kończę.')
    logging.error('Błąd, ale kontynuuję.')
    logging.warning('Uwaga będę coś robił')
    logging.info('Będę coś robił')
    logging.debug('Robię to tak')


Konfiguracja logowania
======================

.. code-block:: python

    import logging

    logging.basicConfig(level=logging.DEBUG)
    logging.basicConfig(format='[%(asctime).19s] [%(levelname)s] %(message)s')

Konfiguracja formatowania logów
===============================

+----------------+-------------------------+-----------------------------------------------+
| Attribute name | Format                  | Description                                   |
+================+=========================+===============================================+
| args           | You shouldn't need to   | The tuple of arguments merged into ``msg`` to |
|                | format this yourself.   | produce ``message``, or a dict whose values   |
|                |                         | are used for the merge (when there is only one|
|                |                         | argument, and it is a dictionary).            |
+----------------+-------------------------+-----------------------------------------------+
| asctime        | ``%(asctime)s``         | Human-readable time when the                  |
|                |                         | `LogRecord` was created.  By default          |
|                |                         | this is of the form '2003-07-08 16:49:45,896' |
|                |                         | (the numbers after the comma are millisecond  |
|                |                         | portion of the time).                         |
+----------------+-------------------------+-----------------------------------------------+
| created        | ``%(created)f``         | Time when the `LogRecord` was created         |
|                |                         | (as returned by `time.time`).                 |
+----------------+-------------------------+-----------------------------------------------+
| exc_info       | You shouldn't need to   | Exception tuple (à la ``sys.exc_info``) or,   |
|                | format this yourself.   | if no exception has occurred, ``None``.       |
+----------------+-------------------------+-----------------------------------------------+
| filename       | ``%(filename)s``        | Filename portion of ``pathname``.             |
+----------------+-------------------------+-----------------------------------------------+
| funcName       | ``%(funcName)s``        | Name of function containing the logging call. |
+----------------+-------------------------+-----------------------------------------------+
| levelname      | ``%(levelname)s``       | Text logging level for the message            |
|                |                         | (``'DEBUG'``, ``'INFO'``, ``'WARNING'``,      |
|                |                         | ``'ERROR'``, ``'CRITICAL'``).                 |
+----------------+-------------------------+-----------------------------------------------+
| levelno        | ``%(levelno)s``         | Numeric logging level for the message         |
|                |                         | (`DEBUG`, `INFO`,                             |
|                |                         | `WARNING`, `ERROR`,                           |
|                |                         | `CRITICAL`).                                  |
+----------------+-------------------------+-----------------------------------------------+
| lineno         | ``%(lineno)d``          | Source line number where the logging call was |
|                |                         | issued (if available).                        |
+----------------+-------------------------+-----------------------------------------------+
| module         | ``%(module)s``          | Module (name portion of ``filename``).        |
+----------------+-------------------------+-----------------------------------------------+
| msecs          | ``%(msecs)d``           | Millisecond portion of the time when the      |
|                |                         | `LogRecord` was created.                      |
+----------------+-------------------------+-----------------------------------------------+
| message        | ``%(message)s``         | The logged message, computed as ``msg %       |
|                |                         | args``. This is set when                      |
|                |                         | `Formatter.format` is invoked.                |
+----------------+-------------------------+-----------------------------------------------+
| msg            | You shouldn't need to   | The format string passed in the original      |
|                | format this yourself.   | logging call. Merged with ``args`` to         |
|                |                         | produce ``message``, or an arbitrary object   |
|                |                         | (see `arbitrary-object-messages`).            |
+----------------+-------------------------+-----------------------------------------------+
| name           | ``%(name)s``            | Name of the logger used to log the call.      |
+----------------+-------------------------+-----------------------------------------------+
| pathname       | ``%(pathname)s``        | Full pathname of the source file where the    |
|                |                         | logging call was issued (if available).       |
+----------------+-------------------------+-----------------------------------------------+
| process        | ``%(process)d``         | Process ID (if available).                    |
+----------------+-------------------------+-----------------------------------------------+
| processName    | ``%(processName)s``     | Process name (if available).                  |
+----------------+-------------------------+-----------------------------------------------+
| relativeCreated| ``%(relativeCreated)d`` | Time in milliseconds when the LogRecord was   |
|                |                         | created, relative to the time the logging     |
|                |                         | module was loaded.                            |
+----------------+-------------------------+-----------------------------------------------+
| stack_info     | You shouldn't need to   | Stack frame information (where available)     |
|                | format this yourself.   | from the bottom of the stack in the current   |
|                |                         | thread, up to and including the stack frame   |
|                |                         | of the logging call which resulted in the     |
|                |                         | creation of this record.                      |
+----------------+-------------------------+-----------------------------------------------+
| thread         | ``%(thread)d``          | Thread ID (if available).                     |
+----------------+-------------------------+-----------------------------------------------+
| threadName     | ``%(threadName)s``      | Thread name (if available).                   |
+----------------+-------------------------+-----------------------------------------------+
