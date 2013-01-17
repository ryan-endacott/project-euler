import math


# Euclidean algorithm
def greatestCommonDenom(m, n):
	if n > m:
		n, m = m, n


	while n != 0:
		temp = n
		n = m % n
		m = temp

	return m

# Wikipedian algorithm
def leastCommonMult(m, n):
	return math.fabs(m * n) / greatestCommonDenom(m, n)

# This works because it gets the least common multiple
# of all of the numbers recursively
def recursiveSolve(m=20):
	if m < 2:
		return 1
	else:
		return leastCommonMult(m, recursiveSolve(m - 1))

print(recursiveSolve())




