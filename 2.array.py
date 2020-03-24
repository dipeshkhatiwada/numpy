Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> a = np.array(2,3,4,6)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a = np.array(2,3,4,6)
ValueError: only 2 non-keyword arguments accepted
>>> ######## wrong###
>>> ######right one is ######
>>> a.nparray([2,3,4,5])
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a.nparray([2,3,4,5])
NameError: name 'a' is not defined
>>> a=np.array([2,3,4,5])
>>> a
array([2, 3, 4, 5])
>>> a.dtype
dtype('int32')
>>> #####complex datatype #####
>>> c = np.array([[1,2],[3,6]],dtype=complex)
>>> c
array([[1.+0.j, 2.+0.j],
       [3.+0.j, 6.+0.j]])
>>> ###for zeros
>>> z = np.zeros((3,4))#3*4
>>> z
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])
>>> one = np.ones((2,3,4),dtype=np.int16) # 3d
>>> one
array([[[1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]],

       [[1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]]], dtype=int16)
>>> one.size
24
>>> np.empty((2,3))
array([[1.28625085e+248, 5.98131385e-154, 4.96009496e+180],
       [1.14448785e+243, 2.41317558e+185, 9.46343361e+218]])
>>> 