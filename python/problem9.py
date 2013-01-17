


def euclidsFormula(m, n):
	mSqrd = m**2
	nSqrd = n**2
	return (mSqrd - nSqrd, 2*m*n, mSqrd + nSqrd)



# Euclid's formula doesn't get every triple, so may need to multiply
# by an arbitrary k if the needed value is skipped
someTriples = [euclidsFormula(m, n) for m in range(100) for n in range(100) if m > n]

answer = [a*b*c for a,b,c in someTriples if a + b + c == 1000]

print(answer)