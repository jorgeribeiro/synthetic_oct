__author__ = 'Jorge Ribeiro'
__email__ = 'joorgemelo@gmail.com'

import scipy.io as sio
import os
import numpy as np
import matplotlib.pyplot as plt

matfile = sio.loadmat('data/Farsiu_Ophthalmology_2013_Control_Subject_1002.mat', squeeze_me=True, struct_as_record=False)
print matfile
image = np.array(matfile['images'])
print image.shape
plt.figure()
plt.imshow(image[:,:,2], 'gray')
plt.show()