# Collatz Conjecture: Take any natural number n. If n is even, divide it by 2 to 
# get n / 2. If n is odd, multiply it by 3 and add 1 to obtain 3n + 1. Repeat the 
# process (which has been called "Half Or Triple Plus One", or HOTPO[6]) indefinitely. 
# The conjecture is that no matter what number you start with, you will always 
# eventually reach 1. The property has also been called oneness.
# Find the number of steps it takes to reach one. 

def iterCollatzSteps(n):
	count = 0
	while n != 1:
		if n % 2 == 0:
			n = n / 2
		else:
			n = (3 * n) + 1
		count = count + 1
	return count 
		
def recCollatzSteps(n, count = 0):
	if n != 1:
		if n % 2 == 0:
			return recCollatzSteps(n/2, count + 1)
		else:
			return recCollatzSteps(3*n + 1, count + 1)
	return count
	

x = input("Number?")
print(iterCollatzSteps(x))
print(recCollatzSteps(x))