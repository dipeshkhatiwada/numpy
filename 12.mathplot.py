Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> def mandelbrot( h,w, maxit=20 ):
	"""Returns an image of the Mandelbrot fractal of size (h,w)."""
	y,x = np.ogrid[ -1.4:1.4:h*1j, -2:0.8:w*1j ]
	c = x+y*1j
	z = c
	divtime = maxit + np.zeros(z.shape, dtype=int)
	for i in range(maxit):
		z = z**2 + c
		diverge = z*np.conj(z) > 2**2            # who is diverging
		div_now = diverge & (divtime==maxit)  # who is diverging now
		divtime[div_now] = i                  # note when
		z[diverge] = 2                        # avoid diverging too muc

		
>>> ef mandelbrot( h,w, maxit=20 ):
	"""Returns an image of the Mandelbrot fractal of size (h,w)."""
	y,x = np.ogrid[ -1.4:1.4:h*1j, -2:0.8:w*1j ]
	c = x+y*1j
	z = c
	divtime = maxit + np.zeros(z.shape, dtype=int)
	for i in range(maxit):
		z = z**2 + c
		diverge = z*np.conj(z) > 2**2            # who is diverging
		div_now = diverge & (divtime==maxit)  # who is diverging now
		divtime[div_now] = i                  # note when
		z[diverge] = 2                        # avoid diverging too much
		
SyntaxError: invalid syntax
>>> def mandelbrot( h,w, maxit=20 ):
	"""Returns an image of the Mandelbrot fractal of size (h,w)."""
	y,x = np.ogrid[ -1.4:1.4:h*1j, -2:0.8:w*1j ]
	c = x+y*1j
	z = c
	divtime = maxit + np.zeros(z.shape, dtype=int)
	for i in range(maxit):
		z = z**2 + c
		diverge = z*np.conj(z) > 2**2            # who is diverging
		div_now = diverge & (divtime==maxit)  # who is diverging now
		divtime[div_now] = i                  # note when
		z[diverge] = 2                        # avoid diverging too muc
	return divtime

>>> plt.imshow(mandelbrot(400,400))
<matplotlib.image.AxesImage object at 0x00EB9DA8>
>>> 