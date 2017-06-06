import numpy as np

def anisodiff1(img, niter=10, kappa=20, option=1):
	"""
	Anisotropic diffusion.

	Usage:
	imgout = anisodiff(im, niter, kappa, gamma, option)

	Arguments:
	        img    - input image
	        niter  - number of iterations
	        kappa  - conduction coefficient 20-100 ?
	        option - 1 sigmoidFormula
	                 2 tanhFormula

	Returns:
	        imgout   - diffused image.
	"""

	img = img.astype('float32')
	imgout = img.copy()
	shiftedY = np.zeros_like(imgout)
	shiftedX = np.zeros_like(imgout)
	for i in range(niter):
		dY, dX = forwardDifferenceGradient(imgout)
		if option == 1:
			cY, cX = sigmoidFormula(dY, dX, kappa)
		elif option == 2:
			cY, cX = tanhFormula(dY, dX, kappa)
		shiftedY[:] = cY
		shiftedX[:] = cX
		shiftedY[1:,:] -= cY[:-1,:]
		shiftedX[:,1:] -= cX[:,:-1]
		imgout += 0.25*(shiftedY+shiftedX)

	return imgout

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