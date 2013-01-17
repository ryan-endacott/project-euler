import math
from mytools import memo

@memo
def getPrimeFactors(val):
	result = []
	sqrtOfVal = math.sqrt(val)
	for i in range(2, int(val / 2) + 1):
		if val % i == 0:
			result.extend(getPrimeFactors(i))
			
			# Minor hack to fix sqrt bug of only being added once
			if sqrtOfVal == i:
				result.extend(getPrimeFactors(i))

	if not result: return [val]
	else: return result

if __name__ == "__main__":
	print (getPrimeFactors(600851475143))
