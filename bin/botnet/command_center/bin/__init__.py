#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Pawel Wylecial
  h0wl@cc-team.org
  
  Matt Harasymczuk
  matt@harasymczuk.pl
  www.matt.harasymczuk.pl
"""

import os
import sys
import logging

logging.basicConfig(filename=None, level=logging.INFO, format="[%(asctime)-15s] %(levelname)s %(message)s")

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
DJANGO_SETTINGS_MODULE = 'settings'
sys.path.append('..')

COMMAND_CENTER_HOST = ''
COMMAND_CENTER_PORT = 31337

PAYLOAD_LISTEN_HOST = "127.0.0.1"
PAYLOAD_LISTEN_PORT = 1337
