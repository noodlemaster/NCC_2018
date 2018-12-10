from src.ciphers.transposition import *
from src.tools.text_manipulation import *

def scytale(text, lower = 2, upper = 10):
    # plaintext = extract_alphabets(removespace(text))
    plaintext = text
    factor = get_factors(len(plaintext))
    result = []
    factors_tocheck = []
    for f in factor:
        if lower <= f <= upper:
            factors_tocheck.append(f)
    for each in factors_tocheck:
        l = text_k_split(plaintext, each)
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
    # file = open('../../../questions/2017/7b_2.txt', 'r')
    text = file.read()
    file.close()
    scytale(text)
    # print(get_factors(1055))