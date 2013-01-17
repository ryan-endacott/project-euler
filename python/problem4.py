

def isPalindrome(num):
	return str(num) == str(num)[::-1]

tripleDigit = range(100, 1000)

numbers = [i * j  for i in tripleDigit for j in tripleDigit]

answer = max(x for x in numbers if isPalindrome(x))


print(answer)
