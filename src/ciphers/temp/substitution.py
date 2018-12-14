import random
import re
from src.tools.hill_climbing import *
from src.ciphers.keyword import get_map_with_keyword

def substitution(text, keyword):
    mapping = get_map_with_keyword(keyword)
    PlainText = re.sub(r'\W', '', text)
    for each in mapping:
        old, new = each[1], each[0]
        PlainText = re.sub(old, new, PlainText)
    return PlainText


if __name__ == '__main__':
    year = '2016'
    question = '8b_4'
    file = open('../../../questions/' + year + '/' + question + '.txt', 'r')
    text = file.read()
    file.close()

    config = {
        'T0': 30,
        'T_lowest': 0,
        'NumberOfIterationPerT': 50,
        'FunctionT': T_mutilier,
        'CipherType': substitution,
        'Keyword/Grid': 'keyword',
        'LengthOfKey_lower': 20,
        'LengthOfKey_upper': 26,
        'Probability_threshold': 0.8,
        'Starting_Keyword': ''
    }

    hill_climbing(text, config)
    #print(substitution(text, 'REAQRRPREQVAPPITVIIKR'))