#!/usr/bin/env python3

import logging
import xml.etree.ElementTree
import subprocess

FILENAME = 'xml-execute-commands.xml'

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('code-execution')
root = xml.etree.ElementTree.parse(FILENAME).getroot()


def run(command, timeout=1):
    log.info('Executing command: %s' % command)
    with subprocess.Popen(command, stdout=subprocess.PIPE) as proc:
        try:
            output, errors = proc.communicate(timeout=timeout)

            if errors:
                log.error(errors)

            if output:
                log.warning(output)
                return output

        except subprocess.TimeoutExpired:
            log.critical('Timeout %s exceeded for command: %s' % (timeout, command))
            proc.kill()


for command in root.findall('./command'):
    cmd = command.text.split()
    timeout = float(command.get('timeout', 0))
    run(cmd, timeout)
