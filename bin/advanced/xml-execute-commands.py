#!/usr/bin/env python3

import logging
import xml.etree.ElementTree
import subprocess

FILENAME = 'xml-execute-commands.xml'
LOG_FORMAT = '[%(levelname)-5s] %(filename)s:%(lineno)s - %(msg).110s'


logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
log = logging.getLogger('code-execution')
root = xml.etree.ElementTree.parse(FILENAME).getroot()


def run(command, timeout=1):
    log.info('Executing command: %s' % command)

    with subprocess.Popen(command, stdout=subprocess.PIPE) as proc:

        try:
            output, errors = proc.communicate(timeout=timeout)
        except subprocess.TimeoutExpired:
            log.error('Timeout %s exceeded for command: %s' % (timeout, command))
            return proc.kill()

        if errors:
            log.error(errors)

        if output:
            log.debug(output)
            return output


for command in root.findall('./command'):
    cmd = command.text.split()
    timeout = float(command.get('timeout', 1))
    run(cmd, timeout)
