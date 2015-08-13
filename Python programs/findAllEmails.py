# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

pattern = re.compile(r'[\w\.-]+@[\w\.-]+')
N = int(raw_input())
allEmails = []

for i in range(N):
    s = raw_input()
    x = re.findall(pattern, s)
    if x:
        allEmails.append(x)

print sorted(sum(allEmails, []))

