from __future__ import division
import scipy as sp
import scipy.special

for n in range(2, 50+1):
	value = scipy.special.jv(n, 20)
	error = abs(( 2 * n / 20 * scipy.special.jv(n-1, 20) - scipy.special.jv(n-2, 20) ) - value) /  abs(value)
	print "n=%d,\tvalue=%g\terror=%g" % (n, value, error)