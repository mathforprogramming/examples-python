# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 15:03:18 2018

@author: berntj
"""

# import numpy libraries
import numpy as np


# construction of matrices and vectors
a = np.array([1,2,3])
b = np.array([[1,2,3],[4,5,6]])

c = np.array([1,2,3],dtype=float)
d = np.array([[1,2,3],[4,5,6]],dtype=float)

 
# manipulating shape
print(b)
print(b.shape)
b.reshape(3,2)
print(b)
print(b.shape)


# matrix of zeroes
a = np.zeros(10,dtype=float)
b = np.zeros((10,10),dtype=float)
print(a)
print(b)

# identity matrix
unit = np.identity(5,dtype=float)
print(unit)

# acessing indivisual elements
a = np.zeros((3,3));
a[1,2] = 10.0
print(a)
 
# slicing
a = np.array([[1,2,3],[4,5,6],[7,8,9]], dtype=float)

# slicing rows
print(a[1:])
print(a[:2])
print(a[1:3])

# slicing columns
print(a[:,1:])
print(a[:,:2])
print(a[:,1:3])

# slicing both
print(a[1:,1:])
print(a[:2,:2])
print(a[:3,1:3])


# Lets move over to matrix operations. We will limit ourselves to those
# which are of interest in this module. We will look at further operations
# later in the course.

# transpose
a = np.array([[1,0,2],[0,5,0],[1,18,2]], dtype=float)
print(a)
b = a.T
c = a.transpose()
print(a)
print(b)
print(c)

# some matrix computations
a = np.array([[1,0,2],[0,5,0],[1,2,3]], dtype=float) 
b = np.identity(3)
print(a)
print(b)

# compute the inverse of a
inva = np.linalg.inv(a)

# compute the matrix product og a and inva
print(np.dot(a,inva)) 

# compute the matrix product of a and b
print(np.dot(a,b))

# add a and b
print(np.add(a,b))

# subtract b from a
print(np.subtract(a,b))

# scalar multiplication
print(np.multiply(2.0,a))

 




