#!/usr/bin/env python

import redis
import urlparse

r = redis.Redis(
        host='huvi.redis.cache.windows.net',
        password='+XfQtzIjJXMgK+4IPcAG0xUKvEsuE6stcGmsMO+yJ6s='
)


rets = []
values = r.lrange('info_parse_failed_urls', 0, -1) 
for value in values:
    rets.append(value)

rets = sorted(rets)
with open('parse_error.txt', 'w') as pf: 
    for ret in rets:
        pf.write(ret + '\r\n')
