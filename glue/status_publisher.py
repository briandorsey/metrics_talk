import json
import time
import zlib
import zmq

def get_stats():
    return [{'value': time.time() % 100,
             'name': 'interesting_metric',
             'time': time.time()}]

c = zmq.Context()
s = c.socket(zmq.PUB)
s.connect('tcp://127.0.0.1:5555')
s.setsockopt(zmq.HWM, 1)

while True:
    data = get_stats()
    data = json.dumps(data)
    data = zlib.compress(data)
    s.send(data)
    time.sleep(5)
