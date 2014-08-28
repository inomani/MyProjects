# Python Challenge 3: One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.
from urllib.request import urlopen
import string
import re


data = urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read()

myList= re.findall("[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]", str(data))
text = ""
for item in myList:
	text = text + item[4]
print(text)
