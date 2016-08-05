from PIL import Image, ImageOps
import numpy as np

path = "/Users/logic/Desktop/chainer-fast-neuralstyle-master/images/"
size = (256,256)
img = Image.open(path+"cubist-style.jpg").convert('RGB') #.resize(size, 2)
img = ImageOps.fit(img, size, Image.ANTIALIAS)
img.save(path+"test.jpg")