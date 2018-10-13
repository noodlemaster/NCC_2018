import itertools
from checkenglishness import *

def extract_alphabet(text):
    textnospace = []
    for c in text:
        if c.isalpha():
            textnospace.append(c.lower())
    return textnospace

def get_factors(n):
    factors = []
    for i in range(n):
        if n%(i+1) == 0:
            factors.append(i + 1)
    return factors

def groupcharactors(text, n):
    table = []
    if len(text)%n != 0:
        return table
    row_n = int(len(text)/n)
    for r in range(row_n):
        row = []
        for c in range(n):
            row.append(text[c*row_n + r])
        table.append(row)
    return table

def generate_permutation(num):
    return list(itertools.permutations(range(num)))

def swape_colume(table, c):
    newtable = []
    for row in table:
        newrow = []
        for n in c:
            newrow.append(row[n])
        newtable.append(newrow)
    return newtable

def return_to_text(table):
    text = []
    for row in table:
        for c in row:
            text.append(c)
    return text


if __name__ == '__main__':
    text = "SIEID ATTPW ADIVL SOLWO IYMRD AOSTT TDUHM AGTTT HSEOO  TAEST EOGNU AEDLN HNRDH KIWOA MENEE INEAS NPAIT SLIAI  AOJDN TCAET SOKEE EIULD HRAUE WSYSA IRBCT WNNSN TARHH  SUHAS MNOAG SVEPI AGINE IOAIS EBGRS TTWYO GTLNO EVMRT  WGTOI SAHHI ECAWP HTRAO TCRTS YRBYG  "
    plaintext = extract_alphabet(text)
    # factors = get_factors(len(plaintext))
    # for i in range(1, len(factors)-1):
    #     print(groupcharactors(plaintext, factors[i]))

    file = open('output.txt', 'w')

    #Lets say we know the factor is 7
    f = 7
    table = groupcharactors(plaintext, f)
    # print(table)


    for combination in generate_permutation(f):
        arranged_table = swape_colume(table, combination)

        text = return_to_text(arranged_table)
        score = get_english_score(text)
        file.write(str(score) + "," + str(combination) + "\n")


    # list_tables = []
    # for combination in generate_permutation(f):
    #     list_tables.append(swape_colume(table, combination))
    #
    # for table in list_tables:
    #     text = return_to_text(table)
    #     score = get_english_score(text)
    #     file.write(str(score) + "," + str(combination) + "\n")

file.close()








