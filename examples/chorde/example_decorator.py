from chorde.decorators import cached
from chorde.clients.memcached import MemcachedClient

import random


m = MemcachedClient(["localhost:11211"], checksum_key="test")

@cached(m, ttl=300, async_ttl=-60)
def expensive_func(x):
        print "calculating..."
        return x * random.random()

