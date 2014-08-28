# Happy Numbers - A happy number is defined by the following process. 
# Starting with any positive integer, replace the number by the sum of 
# the squares of its digits, and repeat the process until the number 
# equals 1 (where it will stay), or it loops endlessly in a cycle which 
# does not include 1. Those numbers for which this process ends in 1 
# are happy numbers, while those that do not end in 1 are unhappy numbers. 
# Display an example of your output here. Find first 8 happy numbers. 

def getSum(n):
    if n == 0:
    	return 0
    else:
    	return ((n%10)**2 + getSum(n//10))

def getHappySum(n):
	sum = getSum(n)
	while sum != 1 and sum != 4:
		sum = getSum(sum)
	return sum

def getfirsteight():
	happyLst = []
	i = 1
	while len(happyLst) < 100:
		s = getHappySum(i)
		if s == 1: 
			happyLst.append(i)
		i = i + 1
	return happyLst
		
		
lst = getfirsteight()
print lst
 