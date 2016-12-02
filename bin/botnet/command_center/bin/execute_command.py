#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Pawel Wylecial
  h0wl@cc-team.org
  
  Matt Harasymczuk
  matt@harasymczuk.pl
  www.matt.harasymczuk.pl
"""


import socket
import sys

from __init__ import *

from django.db import models
from command_center_panel.models.hosts import Host


data = " ".join( sys.argv[1:] )
logging.info( "Sending command to execute: '%s'" % data)

try:
  for bot in Host.objects.filter(active=True):
    sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
    sock.bind((COMMAND_CENTER_HOST, COMMAND_CENTER_PORT + 1))
    sock.sendto( data, ( bot.ip, bot.port ) )
    sock.close()
    logging.info( "Command sent to %s:%s" % ( bot.ip, bot.port ))
      
except KeyboardInterrupt:
  sys.exit()