#!/usr/bin/env python
import string

from PIL import Image
from gearman import GearmanClient 

gearman_client = GearmanClient(['ftester.chinacloudapp.cn:4730']) 
# gearman_client = GearmanClient(['172.31.1.92:4730']) 

path = './sample_images/tubingen.jpg'
data = open(path, 'rb').read()

ljust = string.ljust('kandinsky_e2_crop512', 100, ' ')
data = ljust + data

gearman_request = gearman_client.submit_job('test', data) 
result_data = gearman_request.result 
with open('test.jpg', 'w+') as pf:
	pf.write(result_data)
	#pf.write(data[10:])
