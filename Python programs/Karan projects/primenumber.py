#Check to see if a number is prime

def isPrime(n):
	i = 2
	if n == 1:
		return False
	while i <= n/2:
		if n % i == 0:
			return False
		i = i + 1
	return True
	
x = input("Which number?")
z = isPrime(x)
print z
	
	
	