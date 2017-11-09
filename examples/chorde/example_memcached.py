from chorde.clients.memcached import MemcachedClient
from chorde import CacheMissError
c = MemcachedClient(["localhost:11211"], checksum_key = "testing")
try:
    m = c.get(3)
    print "It's here, the value is: %d" % m
except:
    print "missed 3, let's put it"
    c.put(3, 10, 300)

try:
        c.get(5)
except CacheMissError:
        print "miss"

