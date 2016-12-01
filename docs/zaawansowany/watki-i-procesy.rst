***************
Wątki i procesy
***************

Wątki a procesy
===============

Wątki
=====

Tworzenie wątków
----------------

.. code-block:: python

    from threading import Timer


    def hello():
        print("hello, world")

    t = Timer(5.0, hello)
    t.start()

    print('hej')

Synchronizacja wątków
---------------------

.. code-block:: python

    import queue
    import threading
    import time

    exitFlag = 0


    class myThread (threading.Thread):

        def __init__(self, threadID, name, q):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.q = q

        def run(self):
            print("Starting %s" % self.name)
            process_data(self.name, self.q)
            print("Exiting %s" % self.name)


    def process_data(threadName, q):
        while not exitFlag:
            queueLock.acquire()

            if not workQueue.empty():
                data = q.get()
                queueLock.release()
                print("%s processing %s" % (threadName, data))
            else:
                queueLock.release()

            time.sleep(1)


    threadList = ["Thread-1", "Thread-2", "Thread-3"]
    nameList = ["One", "Two", "Three", "Four", "Five"]
    queueLock = threading.Lock()
    workQueue = queue.Queue(10)
    threads = []
    threadID = 1


    # Create new threads
    for tName in threadList:
        thread = myThread(threadID, tName, workQueue)
        thread.start()
        threads.append(thread)
        threadID += 1


    # Fill the queue
    queueLock.acquire()
    for word in nameList:
        workQueue.put(word)
    queueLock.release()


    # Wait for queue to empty
    while not workQueue.empty():
        pass

    # Notify threads it's time to exit
    exitFlag = 1

    # Wait for all threads to complete
    for t in threads:
        t.join()

    print("Exiting Main Thread")


Zamykanie wątków
----------------

Procesy
=======

Tworzenie procesów
------------------

Synchronizacja procesów
-----------------------

IPC - komunikacja międzyprocesowa
---------------------------------

:figury.py:
    .. code-block:: python

        class Prostokat:

            def __init__(self, a, b):
                self.a = float(a)
                self.b = float(b)

            def pole(self):
                return self.a * self.b

            def obwod(self):
                return (self.a + self.b) * 2

            def __str__(self):
                return 'Prostokat(a=%s, b=%s)' % (self.a, self.b)

:processes-client.py:
    .. code-block:: python

        from multiprocessing.connection import Client
        import logging
        import pickle
        from .figury import Prostokat


        rectangle = Prostokat(a=5, b=10)
        rect = pickle.dumps(rectangle)

        address = ('localhost', 6000)
        conn = Client(address, authkey=b'secret password')

        logging.warning('Sending objects')
        conn.send([rect, 'a', 2.5, None, int, sum])

        logging.warning('Sending close')
        conn.send('close')

        conn.close()

:processes-listener.py:
    .. code-block:: python

        from multiprocessing.connection import Listener
        import logging
        import pickle
        from .figury import Prostokat


        address = ('localhost', 6000)     # family is deduced to be 'AF_INET'

        logging.warning('Listening on %s:%s' % address)
        listener = Listener(address, authkey=b'secret password')
        conn = listener.accept()

        logging.warning('connection accepted from %s %s' % listener.last_accepted)


        while True:
            msg = conn.recv()
            logging.warning('Received: %s' % msg)

            if msg == 'close':
                conn.close()
                break
            else:
                # do something with msg
                prostokat = pickle.loads(msg[0])
                logging.warning('Prostokat %s' % prostokat)
                print('Pole: %s' % prostokat.pole())


        listener.close()




Zamykanie procesów
------------------
