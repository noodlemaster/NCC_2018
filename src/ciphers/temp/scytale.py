from src.ciphers.transposition import *
from src.tools.text_manipulation import *
import re

def scytale(text):
	PlainText = re.sub(r'\W', '', text)
	factor = get_factors(len(PlainText))
	result = []
	for each in factor:
		l = text_k_split(PlainText, each)
		word_list = []
		for s in l:
			string = ''.join(s)
			word_list.append(string)
		text = ''.join(word_list)
		result.append(text)
	print(result)
	return result

if __name__ == '__main__':
	file = open('../../../questions/example/scytale.txt', 'r')
	#file = open('../../../questions/2017/7b.txt', 'r')
	text = file.read()
	file.close()
	scytale(text)