﻿__author__ = 'Jorge Ribeiro'
__email__ = 'joorgemelo@gmail.com'

import scipy.io as sio
import scipy.ndimage as sp 
import scipy.misc as sv
from scipy.ndimage.filters import gaussian_filter as gaussian
import os
import numpy as np
import matplotlib.pyplot as plt

<<<<<<< HEAD
matfile = sio.loadmat('data/Farsiu_Ophthalmology_2013_Control_Subject_1001.mat', squeeze_me=True, struct_as_record=False)
print matfile
image = np.array(matfile['images'])
print image.shape
plt.figure()
plt.imshow(image[:,:,2], 'gray')
plt.show()
=======
matfile = sio.loadmat('data/Subject_10.mat', squeeze_me=True, struct_as_record=False)
img = np.array(matfile['images'])
#plt.figure()
#plt.imshow(img[:,:,2], 'gray')
#plt.show()

#Convert rgb to grayscale
def rgb2gray(rgb):
	return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
img = rgb2gray(img);

def forwardDifferenceGradient(img):  
	diffY = np.zeros_like(img)
	diffX = np.zeros_like(img)
	diffY[:-1, :] = np.diff(img, axis = 0)
	diffX[:, :-1] = np.diff(img, axis = 1)
	return diffY, diffX

def sigmoidFormula(gradientY, gradientX, k):
	cGradientY = np.exp(-(gradientY/k) **2.)
	cGradientX = np.exp(-(gradientX/k) **2.)
	YVal = cGradientY * gradientY
	XVal = cGradientX * gradientX
	return YVal, XVal

def tanhFormula(gradientY, gradientX, k):
	cGradientY = 1./(1. + ((gradientY/k)**2))
	cGradientX = 1./(1. + ((gradientX/k)**2))
	YVal = cGradientY * gradientY
	XVal = cGradientX * gradientX
	return YVal, XVal

img = img.astype("float32")
gauss = gaussian(img, 11)
shiftedY = np.zeros_like(img)
shiftedX = np.zeros_like(img)
for i in range(10):
	dY, dX = forwardDifferenceGradient(img)
	cY, cX = sigmoidFormula(dY, dX, 20)
	shiftedY[:] = cY
	shiftedX[:] = cX
	shiftedY[1:,:] -= cY[:-1,:]
	shiftedX[:,1:] -= cX[:,:-1]
	img += 0.25*(shiftedY+shiftedX)

sv.imsave('anisotropic.jpg', img)
sv.imsave('gaussian.jpg', gauss)
>>>>>>> origin/master
