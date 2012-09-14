import json
import zlib
import redis

r = redis.Redis()  # defaults to localhost

while True:
    _, data = r.brpop('incoming')
    data = zlib.decompress(data)
    data = json.loads(data)
    for stat in data:
        metric = 'demo.%(name)s %(value)s %(time)s' % stat
        r.lpush('outgoing', metric)
