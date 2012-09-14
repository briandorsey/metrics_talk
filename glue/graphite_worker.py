import socket
import redis

r = redis.Redis()  # defaults to localhost
sock = socket.socket()
sock.connect( ('127.0.0.1',2003) )

while True:
    _, message = r.brpop('outgoing')
    message = message + '\n'  # all lines must end in a newline
    print message,
    sock.sendall(message)
