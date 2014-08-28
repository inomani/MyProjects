# All primes below limit

def sievePrimes(n):
	if n <= 1:
		return []
	primes = range(1,n+1)
	primes.remove(1)
	for i in primes:
		for j in primes[i:n+1]:
			if j % i == 0:
				primes.remove(j)
	return primes
 
x = input('Limit?')	
print sievePrimes(x)    
