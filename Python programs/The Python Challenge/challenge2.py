# Python Challenge 2: recognize the characters. maybe they are in the book, 
# but MAYBE they are in the page source.
from urllib.request import urlopen
import string

data = urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read()


text = ""
for item in str(data):
	if str.isalpha(str(item)) and str(item) != "n":
		text = text + item
print(text)		


