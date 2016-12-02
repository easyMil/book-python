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
import sys

from __init__ import *

from django.db import models
from command_center_panel.models.hosts import Host 
from command_center_panel.models.logs import Log

class UDPHandler( SocketServer.BaseRequestHandler ):
  def handle( self ):
    try:
      ip = self.client_address[0]
      port = self.client_address[1]
      msg = self.request[0].strip()
      
      logging.info( "Response received from %s:%s" % ( ip, port ))
      Log(host=Host.objects.get(ip=ip, port=port), log=msg).save()
    except:
      pass


if __name__ == "__main__":
  logging.info ( "Listening for logs on %s:%s..." % ( COMMAND_CENTER_HOST, COMMAND_CENTER_PORT + 2 ) )
  listener = SocketServer.UDPServer( ( COMMAND_CENTER_HOST, COMMAND_CENTER_PORT + 2 ), UDPHandler )

  try:
    listener.serve_forever()
  except KeyboardInterrupt:
    sys.exit()
