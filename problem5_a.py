from __future__ import division
import numpy as np
import numpy.linalg as la

n = 100
np.random.seed(0)
A = np.random.randn(n, n)
x = np.ones((n,1))

b = np.dot(A,x)
sol = la.solve(A, b)

r = np.dot(A,sol) - b

print "relative residuals: %g" % (la.norm(r) / la.norm(b))
print "relative error: %g" % (la.norm(sol-x) / la.norm(x))
print "cond(A): %g" % la.cond(A)
print "Solution:"
print sol.T