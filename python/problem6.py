


def getDifference(m = 100):
	sumOfNumsSquared = sum(range(m + 1)) ** 2
	sumOfSquares = sum(n * n for n in range(m + 1))
	return sumOfSquares - sumOfNumsSquared

print(getDifference())
