from __future__ import division
import scipy as sp
import numpy as np
import numpy.linalg as la
from problem4_a import gauss
from problem4_b import gauss_partial_pivoting

n = 100
A = np.ones((n,n)) * 1e-3
for i in range(0, n):
	for j in range(0, n):
		if ((i+2) % n) == j:
			A[i][j] = 5

np.random.seed(0)
x = np.random.randn(n, 1)
b = np.dot(A, x)

print "condition number for matrix A : \t%g" % la.cond(A)
x_1 = gauss(np.copy(A), np.copy(b))
if(type(x_1) is int):
	print "un-pivoted solves failed"
else:
	print "residual from un-pivoted solve: \t%g" % (la.norm(b - np.dot(A, x_1)) / la.norm(b))
	print "error from un-pivoted solve: \t%g" % (la.norm(x-x_1)/la.norm(x))

x_2 = gauss_partial_pivoting(np.copy(A), np.copy(b))
if(type(x_2) is int):
	print "partial_pivoting solves failed"
else:
	print "residual from  partially-pivoted solve: \t%g" % (la.norm(b - np.dot(A, x_2)) / la.norm(b))
	print "error from  partially-pivoted solve: \t%g" % (la.norm(x-x_2)/la.norm(x))

x_3 = la.solve(np.copy(A), np.copy(b))
print "residual from np.linalg.solve: \t%g" % (la.norm(b - np.dot(A, x_3)) / la.norm(b))
print "error from np.linalg.solve: \t%g" % (la.norm(x-x_3)/la.norm(x))
