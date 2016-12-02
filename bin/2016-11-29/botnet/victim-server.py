import socketserver
import subprocess
import logging
import xml.etree.ElementTree
import json
import io


logging.basicConfig(level=logging.INFO)
log = logging.getLogger('botnet-server')


class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        request = self.request.recv(1024).strip().decode()
        log.debug('Received: %s', request)
        response = self.handle_request(request)
        self.request.sendall(response.encode())

    def execute(self, command, timeout):
        log.debug('Executing command: %s with timeout: %s', command, timeout)
        with subprocess.Popen(command, stdout=subprocess.PIPE) as proc:

            try:
                output, errors = proc.communicate(timeout=timeout)
            except subprocess.TimeoutExpired:
                log.error(
                    'Timeout %s exceeded for command: %s' % (timeout, command))
                return proc.kill()

            if errors:
                log.error(errors)

            if output:
                # red = '\033[00;31m'
                # green = '\033[00;32m'
                # blue = '\033[00;36m'
                # white = '\033[00;39m'
                message = output.decode()

                log.debug('Output: {message}'.format(**locals()))
                return message

    def handle_request(self, request):
        xmlfile = io.StringIO(request)
        root = xml.etree.ElementTree.parse(xmlfile).getroot()
        output = []

        for command in root.findall('./command'):
            cmd = command.text.split()
            timeout = float(command.get('timeout', 1))
            stdout = self.execute(cmd, timeout)
            output.append({
                'command': cmd,
                'timeout': timeout,
                'stdout': stdout,
            })
        return json.dumps(output)


if __name__ == "__main__":
    HOST, PORT = "localhost", 1337

    log.info('Create the server, binding to localhost on port 9999')
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # this will keep running until you interrupt the program with Ctrl-C
    log.info('Server activated')
    server.serve_forever()
