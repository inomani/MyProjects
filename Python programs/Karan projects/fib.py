# Fibonacci Sequence - Enter a number 
# and have the program generate the Fibonacci 
# sequence to that number or to the Nth number.

def fibonacci(n):
	seq = [1]
	x = 1
	
	while (n > 1):
		seq.append(x)
		a = seq[len(seq) - 1]
		b = seq[len(seq) - 2]
		x = a + b
		n= n - 1
		
	print(seq)
		
		
		
if __name__ == "__main__":
    import sys
    fibonacci(int(sys.argv[1]))
