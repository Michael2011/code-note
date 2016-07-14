#!/usr/bin/env python
import os
import os.path
import time
import urlparse
import threading

import redis
import MySQLdb
import simplejson
import requests


redis_status = False

r = redis.Redis(
        host='huvi.redis.cache.windows.net',
        password='+XfQtzIjJXMgK+4IPcAG0xUKvEsuE6stcGmsMO+yJ6s='
)


base_dir = './tmps/'
for i in xrange(100000):
    path = base_dir + str(i)
    os.makedirs(path)
