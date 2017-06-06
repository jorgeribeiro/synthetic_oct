__author__ = 'Jorge Ribeiro'
__email__ = 'joorgemelo@gmail.com'

import scipy.io as sio
import scipy.misc as sv
import numpy as np
from aniso1 import anisodiff1
from aniso2 import anisodiff2

#Load mat image
matfile = sio.loadmat('data/oct_1.mat', squeeze_me=True, struct_as_record=False)
img = np.array(matfile['images'])

#Convert rgb to grayscale
def rgb2gray(rgb):
	return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
img = rgb2gray(img);

sv.imsave('normal.jpg', img)
img1 = anisodiff1(img, niter=50, kappa=20, option=1)
img2 = anisodiff2(img, niter=50, kappa=20, gamma=0.1, step=(1.,1.), option=1, ploton=False)

sv.imsave('anisotropic1.jpg', img1)
sv.imsave('anisotropic2.jpg', img2)
