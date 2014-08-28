# You are given an array with numbers 0 through 10,000, 
# except for one number. Write a function to find that number. 


def findMissing(lst):
	actualSum = (10000 * 10001) / 2 
	listSum = sum(lst)
	return (actualSum - listSum)
	
	
mylist = range(10001)
mylist.remove(7481)
print(findMissing(mylist))