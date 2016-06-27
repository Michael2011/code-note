#!/usr/bin/env python

import redis

r = redis.Redis(
		host='huvi.redis.cache.windows.net',
		password='+XfQtzIjJXMgK+4IPcAG0xUKvEsuE6stcGmsMO+yJ6s='
)

keys = r.hkeys('info_upload_search_urls')
for key in keys:
	print keys 
	break
