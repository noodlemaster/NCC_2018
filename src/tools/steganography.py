from src.ciphers.transposition import *
from src.ciphers.temp.bacon import *

def grouped_string(text):
	possible_table = []
	PlainText = re.sub(r'\W', '', text)
	factors = get_factors(len(PlainText))
	factors.remove(1)
	for factor in factors:
		l = group_text(PlainText, factor)
		possible_table.append(l)
	return possible_table

def Steganography_printing(text):
	PlainText = re.sub(r'\W', '', text)
	binary_string = replace_char_with01(PlainText)
	for each in binary_string:
		for table in grouped_string(each):
			string = ''
			for row in table:
				for i in range(0, len(row)):
					if row[i] == '1':
						string += '#'
					else:
						string += ' '
				string += '\n'
			print(string)
if __name__ == '__main__':
	text = 'wwbbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbbwwwbwwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwwbwwwbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwbwwwbwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwbwwwbwwwwbwwwbbbwwwwwbbbwwwbwwwbwwwbwwwbwwwwbbbwwbwwwbwbbbwwwbbbbwwbbbwwwbbbwwbbbwbwwwbwwwwbwbwwbwwbwwwbwwwwwbwbwwbbwwbwwbwbwwwwbwwwbbwbbwbwwbwwbwwwwwbwwbwwwbwwwwbwwwbwwwbwwbwwwbwbwwwbwbwwwwwbwwwbwbwbwbwbwwwbwwwbwwwbwbwbwbwwbwwbwwwwwbwwwbwwbwwwwbwwbwwwbwwwbbbbbwbbbbwwbwwwwwbbbbbwbwbwbwbbbbbwwwbwwwbwwwbwbbbbwwbbbwwwbbbbwwwbwwwwbwwwbwwwbwwbwwwbwbwbwwwbwwwwwbwwwbwbwbwbwbwwwbwwwbwwwbwwwbwbwwwwwbwwwwwbwbwwwwbwwwwbwwbwwwbwwwbwwwbwbwwbwwwbwwwwbwwwbwbwwbbwbwwwbwwwbwwwbwwwbwbwwwwwbwwwwwbwwbwwwbwwwwbwwwbwwwbwwbwwwbwbwwwbwwwbbbwbwwwbwbwwwbwbwwwbwwbbbwwbwwwbwbwwwwwbbbbwwbwwwbwbbbwwbbbwbwwwbwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwbwwwbwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwbwwwbwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwbwwwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwwwbwwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwwbwwwbwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwbww'
	Steganography_printing(text)