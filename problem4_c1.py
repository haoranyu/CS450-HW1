from __future__ import division
import scipy as sp
import numpy as np
import numpy.linalg as la
from problem4_a import gauss
from problem4_b import gauss_partial_pivoting

n = 100
np.random.seed(0)
A = np.random.randn(n, n)
x = np.random.randn(n, 1)
b = np.dot(A, x)

print "condition number for matrix A : \t%g" % la.cond(A)
x_1 = gauss(A.copy(), b.copy())
if(type(x_1) is int):
	print "un-pivoted solves failed"
else:
	print "residual from un-pivoted solve: \t%g" % (la.norm(b - np.dot(A, x_1)))
	print "error from un-pivoted solve: \t%g" % (la.norm(x-x_1))

x_2 = gauss_partial_pivoting(A.copy(), b.copy())
if(type(x_2) is int):
	print "partial_pivoting solves failed"
else:
	print "residual from  partially-pivoted solve: \t%g" % (la.norm(b - np.dot(A, x_2)))
	print "error from  partially-pivoted solve: \t%g" % (la.norm(x-x_2))

x_3 = la.solve(A.copy(), b.copy())
print "residual from np.linalg.solve: \t%g" % (la.norm(b - np.dot(A, x_3)))
print "error from np.linalg.solve: \t%g" % (la.norm(x-x_3))