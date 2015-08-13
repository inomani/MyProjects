# Enter your code here. Read input from STDIN. Print output to STDOUT
#HackerRank Sherlock and Array Challenge: determine if there is a number in given array such that sum on left is equal to sum on right
# https://www.hackerrank.com/challenges/sherlock-and-array
 
def sherlock():
    N = int(raw_input())
    lst = map(int, raw_input().split())
    pointerA = 0
    pointerB = N-1
    sumLeft = 0
    sumRight = 0
    while (pointerA < pointerB):
        if sumLeft == sumRight:
            sumLeft = sumLeft + lst[pointerA]
            sumRight = sumRight + lst[pointerB]
            pointerA = pointerA + 1
            pointerB = pointerB - 1
        elif sumLeft > sumRight:
            sumRight = sumRight + lst[pointerB]
            pointerB = pointerB - 1
        elif sumRight > sumLeft:
            sumLeft = sumLeft + lst[pointerA]
            pointerA = pointerA + 1
    if (sumLeft == sumRight):
        return 'YES'
    else:
        return 'NO'
    
tests = int(raw_input())
for i in range(tests):
    print sherlock()
