from __future__ import division
import numpy as np
import numpy.linalg as la

n = 100
np.random.seed(0)
A = np.random.randn(n, n)
x = np.ones((n,1))
b = np.dot(A,x)

D = np.diag(2**-np.arange(-n//2, n//2, dtype=np.float64))

sol = la.solve(np.dot(D,A), np.dot(D,b))
r = np.dot(D,b) - np.dot(np.dot(D,A),np.dot(D,sol))

print "relative residuals: %g" % (la.norm(r) / la.norm(np.dot(D,b)))
print "relative error: %g" % (la.norm(sol-x) / la.norm(x))
print "cond(DA): %g" % la.cond(np.dot(D,A))
print "Solution:"
print sol.T