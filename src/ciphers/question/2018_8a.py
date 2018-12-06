import re
from src.tools.hill_climbing import *
from src.ciphers.transposition import *

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']

def remove_capital(text):
    ll = []
    PlainText = re.sub(r'\W', '', text)
    l = list(PlainText)
    for each in l:
        if each in alphabets:
            l.remove(each)
            ll.append(each)
    print(set(ll))
    #print(''.join(l))



if __name__ == '__main__':
    year = '2018'
    question = '8a_a'
    file = open('../../../questions/' + year + '/' + question + '.txt', 'r', errors='replace')
    text = file.read()
    file.close()

    config = {
        'T0': 35,
        'T_lowest': 0,
        'NumberOfIterationPerT': 50,
        'FunctionT': T_mutilier,
        'CipherType': decrypt_transposition,
        'LengthOfKey_lower': 5,
        'LengthOfKey_upper': 17,
        'Probability_threshold': 0.80
    }

    hill_climbing(text, config)