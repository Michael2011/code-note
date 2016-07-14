#!/usr/bin/env python
import os
import os.path
import urlparse

import redis
import MySQLdb
import simplejson
import requests

r = redis.Redis(
        host='huvi.redis.cache.windows.net',
        password='+XfQtzIjJXMgK+4IPcAG0xUKvEsuE6stcGmsMO+yJ6s='
)


infos = {}
mysql_db = {
        'db': 'meiye_online',
        'host': 'rdsef9tiqok322slv8ac.mysql.rds.aliyuncs.com',
        'user': 'online',
        'passwd': 'MEIYE27v984a159meiye'
}
conn=MySQLdb.connect(host=mysql_db['host'], 
                     user=mysql_db['user'],
                     passwd=mysql_db['passwd'],
                     db=mysql_db['db'])
cursor = conn.cursor()

sql = 'select uid,body,type from contents where type = 1 limit {} offset {}'
cursor.execute(sql.format(10000, 0))

i = 10
rows = cursor.fetchall()
while rows:
        for row in rows:
            print 'handle ... ' + row[0]
            pages = simplejson.loads(row[1]) 
            for page in pages['page']:
                for img in page['image']:
                    if infos.has_key(row[0]):
                        infos[row[0]].append(img['cropfileName'])
                    else:
                        infos[row[0]] = [img['cropfileName']]
            try:
                r.hset('meiye_images', row[0], simplejson.dumps(infos[row[0]]))
            except:
                continue
        
        i += 1
        cursor.execute(sql.format(10000, 10000 * i))
        rows = cursor.fetchall()
        print i

print r.hlen('meiye_images')
"""
keys = r.hkeys('meiye_images')

current_dir = os.getcwd()
for key in keys:
    file_path = current_dir + '/images/' + key
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    images = simplejson.loads(r.hget('meiye_images', key))
    for img in images:
        urls = img.split('/')
        req = requests.get(img)
        filename = file_path + '/' + urls[-1]
        with open(filename, 'wb') as pf:
            pf.write(req.content)
"""

