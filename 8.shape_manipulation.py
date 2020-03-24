Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Shape Manipulation
>>> import numpy as np
>>> a = np.floor(10*np.random.random((3,4)))
>>> q
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    q
NameError: name 'q' is not defined
>>> a
array([[2., 4., 1., 7.],
       [9., 5., 2., 5.],
       [9., 0., 2., 9.]])
>>> a.shape(3,4)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a.shape(3,4)
TypeError: 'tuple' object is not callable
>>> a.ravel()
array([2., 4., 1., 7., 9., 5., 2., 5., 9., 0., 2., 9.])
>>> a.reshape(2,6)
array([[2., 4., 1., 7., 9., 5.],
       [2., 5., 9., 0., 2., 9.]])
>>> a.T.shape(4,3)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a.T.shape(4,3)
TypeError: 'tuple' object is not callable
>>> 
>>> a.T
array([[2., 9., 9.],
       [4., 5., 0.],
       [1., 2., 2.],
       [7., 5., 9.]])
>>> a.T.shape(3,4)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a.T.shape(3,4)
TypeError: 'tuple' object is not callable
>>> 