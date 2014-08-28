# Python Challenge 0 --> exponent
import webbrowser


def newURL():
	n = str(2 ** 38)
	webbrowser.open("http://www.pythonchallenge.com/pc/def/" + n + ".html")

newURL()