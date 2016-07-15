#!/usr/bin/env python
import os
import os.path
import time
import urlparse
import threading
import logging

import redis
import MySQLdb
import simplejson
import requests

redis_status = False
user_count = 0

logging.basicConfig(level=logging.INFO,
                format='%(asctime)s %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='logs/download.log',
                filemode='w')

r = redis.Redis(
        host='huvi.redis.cache.windows.net',
        password='+XfQtzIjJXMgK+4IPcAG0xUKvEsuE6stcGmsMO+yJ6s='
)
keys = r.hkeys('meiye_images')
keys = keys[7000:150000]
logging.warning('total count: ' + str(len(keys)))
# keys = ['247412']

def download_meiye_image(**kwargs):
        global redis_status 
        global keys

        while True and keys:
            if not redis_status:
                    # redis_status = True
                    key = keys.pop()
                    # redis_status = False
                    logging.warning('Thread: {} new task: {}'.format(kwargs['target'], key))

                    images = kwargs['redis'].hget('meiye_images', key)
                    try:
                        images = simplejson.loads(images) 
                    except Exception as error:
                        logging.warning(str(error))
                        continue
                    
                    current_dir = os.getcwd()
                    for img in images[:20]:
                        logging.warning('Thread: {} download  (user: {}) image: ({})'.format(kwargs['target'], key, img))
                        file_path = current_dir + '/images/' + key
                        if not os.path.exists(file_path):
                            os.makedirs(file_path)
                        
                        urls = img.split('/')
                        filename = file_path + '/' + urls[-1]
                        
                        try:
                            req = requests.get(img, timeout=5)
                            with open(filename, 'wb') as pf:
                                pf.write(req.content)
                        except Exception as error:
                            logging.warning(str(error))
                            continue

                        time.sleep(5)
                        
        logging.warning('finish ... ' + kwargs['target'])

def main():
    works = []
    for i in xrange(20):
        work = threading.Thread(target=download_meiye_image, kwargs={'redis': r, 'target': str(i)})
        works.append(work)

    for work in works:
        work.setDaemon(True) 
        work.start()
    
    for work in works:
        work.join()


if __name__ == '__main__':
    main()

