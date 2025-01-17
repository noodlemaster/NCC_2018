import math

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def extract_alphabets(text):
    textnospace = []
    for c in text:
        if c.isalpha():
            textnospace.append(c.lower())
    return textnospace

def textksplit(text, k):
    listofchars = []
    for r in range(k):
        chars = []
        for i in range(math.ceil(len(text)/k)):
            try:
                chars.append(text[i*k+r])
            except IndexError:
                pass
        listofchars.append(chars)
    return listofchars

def count_alphabet(text, alphabet):
    alphabet_count = [0] * len(alphabet)
    for i in range(len(alphabet)):
        for c in text:
            if c == alphabet[i].lower():
                alphabet_count[i] += 1
    return alphabet_count

def calculate_ioc(text):
    num = count_alphabet(text, alphabet)
    total = len(text)
    prob = 0.0
    for n in num:
        prob += (n*(n-1))
    if total > 1:
        prob /= (total*(total-1))
    return prob

def get_first_ioc_k(text, k):
    splitedtexts = textksplit(extract_alphabets(text), k)
    prob = calculate_ioc(splitedtexts[0])
    return prob

def get_average_ioc_k(text, k):
    splitedtexts = textksplit(extract_alphabets(text), k)
    probsum = 0.0
    for splitedtext in splitedtexts:
        probsum += calculate_ioc(splitedtext)

    probave = probsum / len(splitedtexts)
    return probave

def get_first_ioc_from_1_to_k(text, k):
    ioc_list = []
    for n in range(1, k + 1):
        ioc_list.append(get_first_ioc_k(text, n))
    return ioc_list

def get_average_ioc_from_1_to_k(text, k):
    ioc_list = []
    for n in range(1, k + 1):
        ioc_list.append(get_average_ioc_k(text, n))
    return ioc_list
