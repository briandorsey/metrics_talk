import redis
import zmq

c = zmq.Context()
s = c.socket(zmq.SUB)
s.bind('tcp://127.0.0.1:5555')
s.setsockopt(zmq.SUBSCRIBE, '')

r = redis.Redis()  # defaults to localhost

while True:
    data = s.recv()
    r.lpush('incoming', data)
