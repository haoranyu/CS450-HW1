from __future__ import division
import scipy as sp
import scipy.special

j_n = scipy.special.jv(1, 20)
j_nm1 = scipy.special.jv(0, 20)
for n in range(2, 50+1):
	j_np1 = (2*(n-1)/20) * j_n - j_nm1
	value_np = scipy.special.jv(n, 20)
	error = abs(value_np - j_np1) / abs(value_np)
	print "n=%d,\tvalue=%g\terror=%g" % (n, j_np1, error)
	j_nm1 = j_n
	j_n = j_np1