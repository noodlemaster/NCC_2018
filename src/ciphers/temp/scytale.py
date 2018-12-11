from src.ciphers.transposition import *
from src.tools.text_manipulation import *

def scytale_decode(text, k):
    plaintext = extract_alphabets(removespace(text))
    l = len(plaintext)
    if l % k == 0:
        table = text_k_split(plaintext, k)
    else:
        row = int(math.floor(l / k))
        table = []
        for i in range(row):
            table.append([''] * k)
        table.append([''] * (l % k))
        i = 0
        while not l == i:
            for c in range(k):
                for r in range(row + 1):
                    try:
                        table[r][c] = plaintext[i]
                        i = i + 1
                    except:
                        break
    word_list = []
    for s in table:
        string = ''.join(s)
        word_list.append(string)
    final_text = ''.join(word_list)
    return final_text

def scytale(text, lower=2, upper=10, onlyfactor=True):
    plaintext = extract_alphabets(removespace(text))
    num_tocheck = []
    result = []
    if onlyfactor:
        factors = get_factors(len(plaintext))
        for f in factors:
            if lower <= f <= upper:
                num_tocheck.append(f)
    else:
        for i in range(upper - lower + 1):
            num_tocheck.append(lower + i)
    for k in num_tocheck:
        result.append(scytale_decode(plaintext, k))
    return result

if __name__ == '__main__':
    # file = open('../../../questions/example/scytale.txt', 'r')
    file = open('../../../questions/2017/7b.txt', 'r')
    text = file.read()
    file.close()
    results = scytale(text, lower=3, upper=6, onlyfactor=False)
    for result in results:
        print(result)
