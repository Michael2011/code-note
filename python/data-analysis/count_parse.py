#!/usr/bin/env python

import redis

r = redis.Redis(
		host='huvi.redis.cache.windows.net',
		password='+XfQtzIjJXMgK+4IPcAG0xUKvEsuE6stcGmsMO+yJ6s='
)

values = r.hgetall('info_download_music_keyword_success')
new_values = { key:int(value) for key,value in values.items()}
new_values = sorted(new_values.iteritems(), key=lambda d:d[1], reverse=True)

with open('success.txt', 'w') as pf:
	for key,value in new_values:
		pf.write(key + '\t' + str(value) + '\n')
		print key, value

values = r.hgetall('info_download_music_keyword_failed')
new_values = { key:int(value) for key,value in values.items()}
new_values = sorted(new_values.iteritems(), key=lambda d:d[1], reverse=True)
with open('failed.txt', 'w') as pf:
	for key,value in new_values:
		pf.write(key + '\t' + str(value) + '\n')
		print key, value
