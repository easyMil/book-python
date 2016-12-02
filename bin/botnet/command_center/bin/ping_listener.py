#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Pawel Wylecial
  h0wl@cc-team.org

  Matt Harasymczuk
  matt@harasymczuk.pl
  www.matt.harasymczuk.pl
"""

import socketserver
import sys
import logging

from __init__ import COMMAND_CENTER_HOST
from __init__ import COMMAND_CENTER_PORT

from django.db import models
from command_center_panel.models.hosts import Host
from command_center_panel.models.pings import Ping


class UDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            msg = self.request[0].strip()
            ip, port = msg.split(':')
            logging.info("Ping received from %s" % msg)
        except:
            return

        try:
            host = Host.objects.get(ip=ip, port=port)
        except:
            host = Host(ip=ip, port=port)
            host.save()

        ping = Ping(host=host)
        ping.save()


if __name__ == "__main__":
    logging.info("Listening for pings on %s:%s...", COMMAND_CENTER_HOST, COMMAND_CENTER_PORT)

    listener = socketserver.UDPServer(
        (COMMAND_CENTER_HOST, COMMAND_CENTER_PORT), UDPHandler)

    try:
        listener.serve_forever()
    except KeyboardInterrupt:
        sys.exit()
