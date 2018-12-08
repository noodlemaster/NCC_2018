import re

from src.ciphers.temp.playfair import form_grid, get_coordinate, hill_climbing, T_minus
from src.tools.text_manipulation import text_split_in_order

def bifid_determine_period(text):

    return period

def bifid(text, keyword, period = 4, row_col = True):
    table = form_grid(keyword)
    # print(table)
    plaintext = []
    # No J
    text1 = re.sub('J', 'I', text)
    blocks = text_split_in_order(text1, period)
    plaintext = ''
    for block in blocks:
        num = ''
        for each in block:
            coord = get_coordinate(table, each)
            if True:
                num = num + str(coord[1]) + str(coord[0])
            else:
                num = num + str(coord[0]) + str(coord[1])
        row = num[0:int(len(num) / 2)]
        col = num[int(len(num) / 2):len(num)]
        plain_period_text = ''
        for i in range(len(row)):
            if True:
                c = table[int(row[i])][int(col[i])]
            else:
                c = table[int(col[i])][int(row[i])]
            plain_period_text = plain_period_text + c.lower()
        plaintext = plaintext + plain_period_text
    return plaintext

if __name__ == '__main__':
    file = open('../../../questions/2016/7b.txt')
    text = file.read()
    file.close()
    print(bifid(text, "LIGO", 4, row_col=True))
    config = {
        'T0': 33,
        'T_lowest': 0,
        'NumberOfIterationPerT': 1000,
        'FunctionT': T_minus,
        'CipherType': bifid,
        'Keyword/Grid': 'keyword',
        'LengthOfKey_lower': 5,
        'LengthOfKey_upper': 16,
        'Probability_threshold': 0.8
    }

    # hill_climbing(text, config)