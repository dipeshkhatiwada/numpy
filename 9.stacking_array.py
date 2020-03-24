Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Stacking together different arrays
>>> a = np.floor(10*np.random.random((2,2)))
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a = np.floor(10*np.random.random((2,2)))
NameError: name 'np' is not defined
>>> import numpy as np
>>> a = np.floor(10*np.random.random((2,2)))
>>> a
array([[5., 8.],
       [4., 0.]])
>>> b = np.floor(10*np.random.random((2,2)))
>>> b
array([[5., 6.],
       [9., 9.]])
>>> np.vstack((a,b))# vertical stack
array([[5., 8.],
       [4., 0.],
       [5., 6.],
       [9., 9.]])
>>> np.hstack((a,b))# horizontal stack
array([[5., 8., 5., 6.],
       [4., 0., 9., 9.]])
>>> #######for adding new axis
>>> from numpy import newaxis
>>> np.column_stack((a,b))
array([[5., 8., 5., 6.],
       [4., 0., 9., 9.]])
>>> a = np.array([4.,2.])
>>> b = np.array([3.,8.])
>>> np.column_stack((a,b))     # returns a 2D array
array([[4., 3.],
       [2., 8.]])
>>> np.hstack((a,b))           # the result is different
array([4., 2., 3., 8.])
>>> a[:,newaxis]
array([[4.],
       [2.]])
>>> np.column_stack((a[:,newaxis],b[:,newaxis]))
array([[4., 3.],
       [2., 8.]])
>>> np.hstack((a[:,newaxis],b[:,newaxis]))   # the result is the same
array([[4., 3.],
       [2., 8.]])
>>> np.r_[1:4,0,4] #1 to 3 and 0 and 4
array([1, 2, 3, 0, 4])
>>> 