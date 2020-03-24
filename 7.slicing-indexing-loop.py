Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> a = np.arange(10)**3
>>> a
array([  0,   1,   8,  27,  64, 125, 216, 343, 512, 729], dtype=int32)
>>> a[2]
8
>>> a[2:4]
array([ 8, 27], dtype=int32)
>>> a[2:4:2]
array([8], dtype=int32)
>>> a[ : :-1]
array([729, 512, 343, 216, 125,  64,  27,   8,   1,   0], dtype=int32)
>>> for i in a:
	i**(1/3)

	
0.0
1.0
2.0
3.0
3.9999999999999996
4.999999999999999
5.999999999999999
6.999999999999999
7.999999999999999
8.999999999999998
>>> ### using function in np
>>> def fun(x,y)
SyntaxError: invalid syntax
>>> def fun(x,y):
	return 10*x+y

>>> b = np.fromfunction(f,(5,4),dtype=int)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    b = np.fromfunction(f,(5,4),dtype=int)
NameError: name 'f' is not defined
>>> b = np.fromfunction(fun,(5,4),dtype=int)
>>> b
array([[ 0,  1,  2,  3],
       [10, 11, 12, 13],
       [20, 21, 22, 23],
       [30, 31, 32, 33],
       [40, 41, 42, 43]])
>>> b[2,3]
23
>>> b[-1]
array([40, 41, 42, 43])
>>> b[-1,:]
array([40, 41, 42, 43])
>>> c = np.array( [[[  0,  1,  2],               # a 3D array (two stacked 2D arrays)
...                 [ 10, 12, 13]],
...                [[100,101,102],
...                 [110,112,113]]])
Traceback (most recent call last):
  File "<pyshell#21>", line 2, in <module>
    ...                 [ 10, 12, 13]],
TypeError: 'ellipsis' object is not subscriptable
>>> c = np.array( [[[  0,  1,  2],[ 10, 12, 13]],[[100,101,102],[110,112,113]]])
>>> c
array([[[  0,   1,   2],
        [ 10,  12,  13]],

       [[100, 101, 102],
        [110, 112, 113]]])
>>> c.shape
(2, 2, 3)
SyntaxError: multiple statements found while compiling a single statement
>>> c.shape(2, 2, 3)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    c.shape(2, 2, 3)
TypeError: 'tuple' object is not callable
>>> c[1,:,:
  ]
array([[100, 101, 102],
       [110, 112, 113]])
>>> 