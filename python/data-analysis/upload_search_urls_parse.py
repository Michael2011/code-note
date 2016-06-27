#!/usr/bin/env python

import redis
import urlparse

r = redis.Redis(
		host='huvi.redis.cache.windows.net',
		password='+XfQtzIjJXMgK+4IPcAG0xUKvEsuE6stcGmsMO+yJ6s='
)


count = {'shared': {
			'success': 0,
			'failed': 0
		},
		'mp3': {
			'success': 0,
			'failed': 0
		},
		'other': {
			'success': 0,
			'failed': 0
		}
}

keys = r.hkeys('info_upload_search_urls')
for key in keys:
	if '4shared' in key:
			values = r.hget('info_upload_search_urls', key)
			values = values.split('#')

			for value in values:
				info = urlparse.urlparse(value)
				
				if info.netloc not in ('www.4shared.com', 'search.4shared.com'):
					print value
					count['shared']['failed'] += 1
					continue


				if '/music/' in value:
					count['shared']['success'] += 1

				elif '/mp3/' in value:
					count['shared']['success'] += 1

				elif '/archive/' in value:
					print value
					count['shared']['failed'] += 1

				elif '/books_office/' in value:
					print value
					count['shared']['failed'] += 1

				elif '/photo/' in value:
					print value
					count['shared']['failed'] += 1

				else:
					count['shared']['success'] += 1

	elif ' mp3' in key:
		values = r.hget('info_upload_search_urls', key)
		values = values.split('#')
		for value in values:
			info = urlparse.urlparse(value)
			
			if 'google.com' in info.netloc:
				print value
				count['mp3']['failed'] += 1
				continue	
			
			count['mp3']['success'] += 1
	else:
		count['other']['success'] += 1
print count
