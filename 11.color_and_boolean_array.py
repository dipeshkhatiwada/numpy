Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy asnp
SyntaxError: invalid syntax
>>> import numpy as np
>>> palette = np.array([[0, 0, 0],         # black
...                     [255, 0, 0],       # red
...                     [0, 255, 0],       # green
...                     [0, 0, 255],       # blue
...                     [255, 255, 255]])  # white
Traceback (most recent call last):
  File "<pyshell#2>", line 2, in <module>
    ...                     [255, 0, 0],       # red
TypeError: 'ellipsis' object is not subscriptable
>>> alette = np.array([[0, 0, 0],[255, 0, 0],[0, 0, 255],[255, 255, 255]])
>>> alette
array([[  0,   0,   0],
       [255,   0,   0],
       [  0,   0, 255],
       [255, 255, 255]])
>>> image = np.array([[0, 1, 2, 0],[0, 3, 4, 0]]) # each value corresponds to a color in the palette
>>> alettr[image]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    alettr[image]
NameError: name 'alettr' is not defined
>>> alette[image]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    alette[image]
IndexError: index 4 is out of bounds for axis 0 with size 4
>>> image
array([[0, 1, 2, 0],
       [0, 3, 4, 0]])
>>> alette
array([[  0,   0,   0],
       [255,   0,   0],
       [  0,   0, 255],
       [255, 255, 255]])
>>> alette[image]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    alette[image]
IndexError: index 4 is out of bounds for axis 0 with size 4
>>> alette = np.array([[0, 0, 0],[255, 0, 0],[0, 255, 0],[0, 0, 255],[255, 255, 255]])
>>> alette[image]
array([[[  0,   0,   0],
        [255,   0,   0],
        [  0, 255,   0],
        [  0,   0,   0]],

       [[  0,   0,   0],
        [  0,   0, 255],
        [255, 255, 255],
        [  0,   0,   0]]])
>>> ### boolean indexing
>>> a = np.arange(12).reshape(3,4)
>>> b = a>4
>>> b
array([[False, False, False, False],
       [False,  True,  True,  True],
       [ True,  True,  True,  True]])
>>> a[b]
array([ 5,  6,  7,  8,  9, 10, 11])
>>> ### 1d array with the selected elements
>>> a[b] = 0
>>> a
array([[0, 1, 2, 3],
       [4, 0, 0, 0],
       [0, 0, 0, 0]])
>>> ##### 0's at all false value
>>> 