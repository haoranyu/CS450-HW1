from __future__ import division
import scipy as sp
import scipy.special

j_n = scipy.special.jv(49, 20)
j_np1 = scipy.special.jv(50, 20)
for n in range(2, 50+1):
	j_nm1 = (2 * (50-n+1) / 20) * j_n - j_np1
	value_np = scipy.special.jv(50 - n, 20)
	error = abs(value_np - j_np1) / abs(value_np)
	print "n=%d,\tvalue=%g\terror=%g" % (50-n, j_np1, error)
	j_np1 = j_n
	j_n = j_nm1