from mytools import memo
from itertools import count, takewhile


@memo
def fib(n):
	if (n <= 1): return 1
	else: return fib(n-1) + fib(n-2)


MAX = 4000000


fibUpToMax = takewhile(lambda x: x < MAX, (fib(n) for n in count()))

print (sum(x for x in fibUpToMax if x % 2 == 0))

