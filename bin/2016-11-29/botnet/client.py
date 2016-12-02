import socket
import sys

HOST, PORT = "localhost", 1337
commands = ['/bin/ls -la', '/bin/echo "ehlo"', '/bin/cat /etc/passwd']


# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(bytes(commands + "\n", "utf-8"))

    # Receive data from the server and shut down
    received = str(sock.recv(1024), "utf-8")


print("Sent:     {}".format(commands))
print("Received: {}".format(received))
