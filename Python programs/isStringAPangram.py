# Enter your code here. Read input from STDIN. Print output to STDOUT

input = raw_input()
lowerinput = input.lower()
setinput = set(lowerinput)
if len(setinput) == 27:
    print "pangram"
else:
    print "not pangram"

