Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##Copies and Views
>>> a = np.arange(12)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a = np.arange(12)
NameError: name 'np' is not defined
>>> import numpy as np
>>> a = np.arange(12)
>>> a
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
>>> b=a
>>> b
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
>>> #####new obj is not created
>>> a = np.arange(12)
>>> b is a
False
>>> b=a
>>> b is a
True
>>> ## same array
>>> def f(x):
	print(id(x))

	
>>> id(a)
54179624
>>> id(b)
54179624
>>> ##same id means same obj
>>> c = a.view()##creating diff obj
>>> c
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
>>> c is a
False
>>> id(c)
121178336
>>> c.base is a # c is a view of the data owned by a
True
>>> c.shape = 2,6                      # a's shape doesn't change
>>> a.shape = 2,6
>>> a
array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11]])
>>> c
array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11]])
>>> a.shape = 4,3
>>> a
array([[ 0,  1,  2],
       [ 3,  4,  5],
       [ 6,  7,  8],
       [ 9, 10, 11]])
>>> c
array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11]])
>>> d = a.copy()
>>> d
array([[ 0,  1,  2],
       [ 3,  4,  5],
       [ 6,  7,  8],
       [ 9, 10, 11]])
>>> a.shape = 2,6
>>> d
array([[ 0,  1,  2],
       [ 3,  4,  5],
       [ 6,  7,  8],
       [ 9, 10, 11]])
>>> a
array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11]])
>>> d is a
False
>>> 