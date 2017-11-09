from chorde.clients.inproc import InprocCacheClient
from chorde import CacheMissError
c = InprocCacheClient(200)
c.put(3, 10, 300) # put value 10 on key 3, TTL 5min
assert 10 == c.get(3)
try:
        c.get(5)
except CacheMissError:
        print "miss"

