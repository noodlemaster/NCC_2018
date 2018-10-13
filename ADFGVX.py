import re
from textksplit import *
#from transposition import *

template = []

def convertTOtransposition(text):
	l = []
	PlainText = re.sub(r'\W', '', text)
	for i in range (2, 25):
		listOFchar = textksplit(PlainText, i)
		for each in listOFchar:
			string = ''.join(each)
			l.append(string)

	print(l)


if __name__ == '__main__':
	text = 'DGDD DAGD DGAF ADDF DADV DVFA ADVX'
	convertTOtransposition(text)