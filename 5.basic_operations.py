Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> a = np.array( [20,30,40,50] )
>>> a
array([20, 30, 40, 50])
>>>  b = np.arange( 4 ) # 0 to 3 in order
 
SyntaxError: unexpected indent
>>> b = np.arange( 4 ) # 0 to 3 in order
>>> b
array([0, 1, 2, 3])
>>> c=a-b# array sub
>>> c
array([20, 29, 38, 47])
>>> b**2 #Square of all
array([0, 1, 4, 9], dtype=int32)
>>> 10*np.sin(a)
array([ 9.12945251, -9.88031624,  7.4511316 , -2.62374854])
>>> a<35 #if condition
array([ True,  True, False, False])
>>> A = np.array([[1,1],[0,1]])
>>> B= np.array([[2,0],[3,4]])
>>> A*B #element wise product
array([[2, 0],
       [0, 4]])
>>> A@B # martrix product
array([[5, 4],
       [3, 4]])
>>> A.dot(B)#dot product
array([[5, 4],
       [3, 4]])
>>> a = np.ones((2,3), dtype=int)
>>> a *=3
>>> a
array([[3, 3, 3],
       [3, 3, 3]])
>>> a +=a
>>> a
array([[6, 6, 6],
       [6, 6, 6]])
>>> a.sum()
36
>>> a.min()
6
>>> a.max()
6
>>> a.avg()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a.avg()
AttributeError: 'numpy.ndarray' object has no attribute 'avg'
>>> a.average()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a.average()
AttributeError: 'numpy.ndarray' object has no attribute 'average'
>>> b = np.arange(12).reshape(3,4)
>>> b
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>> v.sum(axis=0)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    v.sum(axis=0)
NameError: name 'v' is not defined
>>> b.sum(axis=0)
array([12, 15, 18, 21])
>>> b.sum(axis=1)
array([ 6, 22, 38])
>>> b.min(axis=1) # mijn of each row
array([0, 4, 8])
>>> b.cumsum(axis=1) #cumulative sum along each row
array([[ 0,  1,  3,  6],
       [ 4,  9, 15, 22],
       [ 8, 17, 27, 38]], dtype=int32)
>>> 