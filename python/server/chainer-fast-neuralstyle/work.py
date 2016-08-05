#-*- coding:utf-8 -*-
#!/usr/bin/env python2.7

import os
import time
import io
import logging
import commands
import string

import numpy as np
import argparse
from PIL import Image
from skimage.restoration import denoise_tv_chambolle
from gearman import GearmanClient 

import chainer
from chainer import cuda, Variable, serializers
from net import *

import gearman
from config import server

logging.basicConfig(level=logging.DEBUG,  
				format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
				datefmt='%a, %d %b %Y %H:%M:%S',  
				filename='logs/access.log',  
				filemode='w+')

def test_case(kwargs, task):
	model_name = os.listdir('models_availiable')[0].split('.')[0].split('_')[0]
	xp = task.xp

	start = time.time()

	start = time.time()
	file_name = './sample_images/tubingen.jpg'
	image = xp.asarray(Image.open(file_name).convert('RGB'), dtype=xp.float32).transpose(2, 0, 1)
	image = image.reshape((1,) + image.shape)
	x = Variable(image)

	# y = model(x)
	y = task.models[model_name](x)
	result = cuda.to_cpu(y.data)

	result = result.transpose(0, 2, 3, 1)
	result = result.reshape((result.shape[1:]))
	result = result/255.0
	logging.info('test model run: {}'.format(time.time() - start))

def task_callback(gearman_worker, gearman_job): 
	print gearman_job.data 
	print "-----------\n"
	return gearman_job.data

class ImageGearmanWorker(gearman.GearmanWorker):
	def on_job_execute(self, current_job):
		print "Job started"
		print "===================\n"
		return super(ImageGearmanWorker, self).on_job_execute(current_job)

class ImageHandleTask(object):
	def __init__(self, kwargs):
		logging.info("ImageHandleTask init ...")
		self.models = {}	
		self.denoise = {}
		self.args = kwargs['args']

		self.xp = np if self.args.gpu < 0 else cuda.cupy

		""" # load image model
		self.model = FastStyleNet()
		serializers.load_npz(self.args.model, self.model)
		if self.args.gpu >= 0:
			cuda.get_device(self.args.gpu).use()
			slef.model.to_gpu()
		"""
		self.load_models(self.args.model)

	def load_models(self, models):
		models = models.split(',')

		availiable_path = 'models_availiable'
		update_path = 'models_upload'
		all_models = 'models'

		models_availiable = os.listdir(availiable_path)
		models_upload = os.listdir(update_path)

		self.models = {m.split('.')[0].split('_')[0]:availiable_path +'/'+ m 
							for m in models_availiable}

		for m in models_upload:
			model_name = m.split('.')[0].split('_')[0]
			
			if not self.models.has_key(model_name):
				cmd = 'mv {update}/{update_name} {availiable}/'.format(
									update=update_path, update_name=m,
									availiable=availiable_path)
				(status, output) = commands.getstatusoutput(cmd)
				self.models[model_name] = availiable_path + '/' + m 
			else:
				cmd = 'mv {availiable} {all_models}'.format(
									availiable=self.models[model_name],
									all_models=all_models)
				(status, output) = commands.getstatusoutput(cmd)

				cmd = 'mv {update}/{update_name} {availiable}/'.format(
									update=update_path, update_name=m,
									availiable=availiable_path)
				(status, output) = commands.getstatusoutput(cmd)
				self.models[model_name] = availiable_path + '/' + m 

		# init denoise
		file_name = 'denoise.txt'
		if os.path.exists(file_name):
			with open(file_name, 'r') as pf:
				for line in pf.readlines():
					line = line.strip().split(' ')	
					self.denoise[line[0].strip()] = float(line[-1].strip())

		# init model
		for model_name,value in self.models.items():
			# model_name = m.split('/')[-1].split('.')[0]

			handle_model = FastStyleNet()
			serializers.load_npz(value, handle_model)

			if self.args.gpu >= 0:
				cuda.get_device(self.args.gpu).use()
				handle_model.to_gpu()

			self.models[model_name] = handle_model
		
		load_all_models = ', '.join(self.models.keys())
		logging.info('loading models : ' + load_all_models)
		logging.info('load success')
			
	def fetch_task(self):
		pass

	def handle_task(self, gearman_worker, gearman_job):
		model_name = (gearman_job.data[:100].split('_')[0]).strip()
		data = gearman_job.data[100:]

		stream = io.BytesIO(data)
		
		logging.info('model({}) is callbacked'.format(model_name))
		start = time.time()
		image = self.xp.asarray(Image.open(stream).convert('RGB'),
					dtype=self.xp.float32).transpose(2, 0, 1)
		image = image.reshape((1,) + image.shape)
		x = Variable(image)

		if (self.models.has_key(model_name)):
			# y = self.model(x)
			y = self.models[model_name](x)
		else:
			return ''

		result = cuda.to_cpu(y.data)
		result = result.transpose(0, 2, 3, 1)
		result = result.reshape((result.shape[1:]))
		#result = np.uint8(result)
		result = result/255.0

		logging.info('{} runtime: {}s'.format(model_name, time.time() - start))

		# 增加降噪处理 
		denoise_rate = self.denoise.get(model_name, self.args.denoise)
		logging.info('{} denoise {}'.format(model_name, denoise_rate))
		if denoise_rate > 0.001:
			denoise_time = time.time()
			denoise_rate = 1.0 if denoise_rate>1.0 else denoise_rate
			result = denoise_tv_chambolle(result, weight=denoise_rate, 
							multichannel=True, 
							n_iter_max = 4)
			logging.info('{} denoise runtime {}'.format(model_name, time.time()-denoise_time))
		result = np.uint8(result*255)

		import ipdb;ipdb.set_trace()
		# 读写图片
		# file_name = '/tmp/' + str(os.getuid()) + str(int(time.time())) + '.jpg'
		file_name = '/tmp/' + str(self.args.gpu) + str(int(time.time() * 10000)) + '.jpg'
		Image.fromarray(result).save(file_name)
		
		with open(file_name, 'r') as pf:
			content = pf.read()
		
		cmd = 'rm -f {file_name}'.format(file_name=file_name)
		commands.getstatusoutput(cmd)
		
		return content
		# Image.fromarray(result).save(self.args.out)
		# return result.tobytes()

class ManagerWork(object):
	def __init__(self, kwargs):
		self.task = ImageHandleTask(kwargs)
		self.worker  = ImageGearmanWorker(server[kwargs['args'].env]['host'])
		self.worker.register_task(server[kwargs['args'].env]['queue'], self.task.handle_task)
		# self.worker.register_task(server[self.args.env]['queue'], task_callback)
		
		# self.task.handle_task(None, None. debug=True, model_name=123, data=123)
		# test case
		test_case(kwargs, self.task)

	def start(self):
		self.worker.work()

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Real-time style transfer image generator')
	# parser.add_argument('input')
	parser.add_argument('--int', '-i', default='out.jpg', type=str)
	parser.add_argument('--gpu', '-g', default=-1, type=int,
						help='GPU ID (negative value indicates CPU)')
	parser.add_argument('--model', '-m', default='models/style.model', type=str)
	parser.add_argument('--out', '-o', default='out.jpg', type=str)
	parser.add_argument('--denoise', '-d', default=0.0, type=float)
	parser.add_argument('--env', '-e', default='debug', type=str)
	args = parser.parse_args()

	# TODO: 处理逻辑
	# image = ImageHandleTask({'args': args})
	# image.handle_task()

	# online
	manage = ManagerWork({'args': args})
	manage.start()
