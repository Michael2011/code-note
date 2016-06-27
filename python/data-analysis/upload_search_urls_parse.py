#!/usr/bin/env python

import redis

r = redis.Redis(
        host='huvi.redis.cache.windows.net',
        password='+XfQtzIjJXMgK+4IPcAG0xUKvEsuE6stcGmsMO+yJ6s='
)


count = {'shared': {
            'success': 0,
            'failed': 0
        }
}

keys = r.hkeys('info_upload_search_urls')
for key in keys:
    if '4shared' not in key:
        continue

    values = r.hget('info_upload_search_urls', key)
    values = values.split('#')

    for value in values:
       if '4shared.com' not in value:
           continue


       if '/music/' in value:
          count['shared']['success'] += 1

       elif '/mp3/' in value:
          count['shared']['success'] += 1

       else:
          count['shared']['failed'] += 1

print count
