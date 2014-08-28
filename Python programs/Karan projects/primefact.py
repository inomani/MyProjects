#Prime Factorization - Have the user enter a number 
#and find all Prime Factors (if there are any) and display them.
#The prime factors of a number will always be less than or equal the number/2

def isPrime(n):
	i = 2
	if n == 1:
		return False
	while i <= n/2:
		if n % i == 0:
			return False
		i = i + 1
	return True

def primefact(i, n, lst):
	if n > 1:
		if n % i == 0:
			if i not in lst:
				lst.append(i)
			primefact(i, n/i, lst)
		else:
			while i <= n/2:
				i = i + 1
				primefact(i, n, lst)
			if isPrime(n) and n not in lst:
				lst.append(n)
	else:
		lst = []
		
					

		
x = input("What number to find prime factors for?")
primeFactors= []
primefact(2, x, primeFactors)
print primeFactors



	
	
	
	
	
	