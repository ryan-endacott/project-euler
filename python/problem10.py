
from problem7 import isPrime


def sumPrimes(limit = 2000000):
	sum = 0
	for i in range(limit):
		if isPrime(i):
			sum += i
	return sum

print(sumPrimes())