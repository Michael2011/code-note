import numpy as np
import argparse
from PIL import Image
import time

import chainer
from chainer import cuda, Variable, serializers
from net import *


# from skimage.filter import denoise_tv_chambolle  #for versoin: 0.9.3   sudo apt-get install python-skimage   pip install  scikit-image(failed)
from skimage.restoration import denoise_tv_chambolle  #for new version   need conda

parser = argparse.ArgumentParser(description='Real-time style transfer image generator')
parser.add_argument('input')
parser.add_argument('--gpu', '-g', default=-1, type=int,
                    help='GPU ID (negative value indicates CPU)')
parser.add_argument('--model', '-m', default='models/style.model', type=str)
parser.add_argument('--out', '-o', default='out.png', type=str)
parser.add_argument('--denoise', '-d', default=0.15, type=float)
args = parser.parse_args()

start = time.time()

model = FastStyleNet()
serializers.load_npz(args.model, model)
if args.gpu >= 0:
    cuda.get_device(args.gpu).use()
    model.to_gpu()
xp = np if args.gpu < 0 else cuda.cupy

print 'model init: ', time.time() - start, 'sec'

start = time.time()
image = xp.asarray(Image.open(args.input).convert('RGB'), dtype=xp.float32).transpose(2, 0, 1)
image = image.reshape((1,) + image.shape)
x = Variable(image)

y = model(x)
result = cuda.to_cpu(y.data)

result = result.transpose(0, 2, 3, 1)
result = result.reshape((result.shape[1:]))
# result = np.uint8(result)
result = result/255.0
print 'model run: ', time.time() - start, 'sec'


# print result.shape
# print result
denoise_rate = args.denoise
# print denoise_rate
if denoise_rate > 0.001:
	start = time.time()
	if denoise_rate > 1.0:
		denoise_rate = 1.0
	result = denoise_tv_chambolle(result, weight = denoise_rate, multichannel = True, n_iter_max = 4)
	print 'denoise: ', time.time() - start, 'sec'

result = np.uint8(result*255)

Image.fromarray(result).save(args.out)
