



def isPrime(n):
	if n == 2: return True
	if n % 2 == 0: return False
	if n < 2: return False
	for i in range(3, int(n ** .5 + 1), 2):
		if n % i == 0:
			return False
	return True

def getPrime(n):

	numPrimes = 1
	for i in range(3, 99999999999, 2):
		if isPrime(i):
			numPrimes += 1
			if numPrimes == n: return i


if __name__ == "__main__":
	print(getPrime(10001))

