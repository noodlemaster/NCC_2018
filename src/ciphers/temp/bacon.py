from src.ciphers.polybius import *

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def replace_char_with01(text):
	result = []
	PlainText = re.sub(r'\W', '', text)
	l = get_existing_characters(PlainText)
	if len(l) == 2:
		string1 = re.sub(l[0], '0', PlainText)
		string1 = re.sub(l[1], '1', string1)
		string2 = re.sub(l[0], '1', PlainText)
		string2 = re.sub(l[1], '0', string2)
		result.append(string1)
		result.append(string2)
		return result
	else:
		return False

def binary2base10(binary): #data type for binary needs to be string when it is an input
	top_power = len(binary)
	reversed_binary = binary[::-1]
	base10 = 0
	for i in range(0, top_power):
		value = int(reversed_binary[i])*(2**i)
		base10 += value
	return base10

def bacon(text):
	zero_one = replace_char_with01(text)
	final_list = []
	try:
		result = []
		list_grouped = group_text(zero_one[0], 5)
		for each in list_grouped:
			index = binary2base10(each)
			#print(index)
			alpha = alphabet[index]
			result.append(alpha)
		target = ''.join(result)
		final_list.append(target)
		print(target)
	except IndexError:
		result = []
		list_grouped = group_text(zero_one[0], 5)
		for each in list_grouped:
			index = binary2base10(each)
			print(index)
			alpha = alphabet[index]
			result.append(alpha)
		target = ''.join(result)
		final_list.append(target)
		print(target)
	return final_list

	# 	result = []
	# 	list_grouped = group_text(text, 5)
	# 	for each in list_grouped:
	# 		index = binary2base10(each)
	# 		alpha = alphabet[index]
	# 		result.append(alpha)
	# 	target_string = ''.join(result)
	# 	print(target_string)
	# 	return target_string


if __name__ == '__main__':
	text = 'wwbbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbbwwwbwwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwwbwwwbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwbwwwbwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwbwwwbwwwwbwwwbbbwwwwwbbbwwwbwwwbwwwbwwwbwwwwbbbwwbwwwbwbbbwwwbbbbwwbbbwwwbbbwwbbbwbwwwbwwwwbwbwwbwwbwwwbwwwwwbwbwwbbwwbwwbwbwwwwbwwwbbwbbwbwwbwwbwwwwwbwwbwwwbwwwwbwwwbwwwbwwbwwwbwbwwwbwbwwwwwbwwwbwbwbwbwbwwwbwwwbwwwbwbwbwbwwbwwbwwwwwbwwwbwwbwwwwbwwbwwwbwwwbbbbbwbbbbwwbwwwwwbbbbbwbwbwbwbbbbbwwwbwwwbwwwbwbbbbwwbbbwwwbbbbwwwbwwwwbwwwbwwwbwwbwwwbwbwbwwwbwwwwwbwwwbwbwbwbwbwwwbwwwbwwwbwwwbwbwwwwwbwwwwwbwbwwwwbwwwwbwwbwwwbwwwbwwwbwbwwbwwwbwwwwbwwwbwbwwbbwbwwwbwwwbwwwbwwwbwbwwwwwbwwwwwbwwbwwwbwwwwbwwwbwwwbwwbwwwbwbwwwbwwwbbbwbwwwbwbwwwbwbwwwbwwbbbwwbwwwbwbwwwwwbbbbwwbwwwbwbbbwwbbbwbwwwbwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwbwwwbwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwbwwwbwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwbwwwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwwwbwwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwbbbwwbwwwbwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwwbwwbww'
	#bacon(text)
	#print(len(text))
	#print(alphabet[17])
	#binary2base10('11001')
	#replace_char_with01(text)