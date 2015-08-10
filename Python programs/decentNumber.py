# Enter your code here. Read input from STDIN. Print output to STDOUT
def findLargestDecent(N):
    numberOfFives = N
    if (N % 3 != 0):
        if (N-5 < 0):
            print '-1'
        else:
            findLargestDecent(N-5)
    else:
        for i in range(numberOfFives):
            newList[i] = '5'
        print ''.join(newList)
    

T = int(raw_input())
for i in range(T):
    N = int(raw_input())
    newList = ['3' for i in range(N)]
    findLargestDecent(N)
    

        
