import re
from textksplit import *
from Hill import *
from src.transposition import *
# from transposition import *

template = []

def convertTOtransposition(text):
    factor_list = get_factors(len(text))
    factor_list.remove(1)
    '''
    text_list = []
    for factor in factor_list:
        l = group_text(text, factor)
        text_list.append(l)
    print(text_list)
    for each in text_list:
        n = len(each[0])
        list1 = []
        for i in range(n):
            list1.append(each[i])
        print(list1)
    '''
    l = []
    for factor in factor_list:
        l.append(textksplit(text, factor))
    print(l)

if __name__ == '__main__':
    text = 'DGDD DAGD DGAF ADDF DADV DVFA ADVX'
    PlainText = re.sub(r'\W', '', text)
    convertTOtransposition(PlainText)

    '''
    plaintext = extract_alphabets(text)
    factors = get_factors(len(plaintext))

    max_columns = 7

    factors_to_check = []
    for f in factors:
        if f > max_columns:
            break
        else:
            factors_to_check.append(f)
    factors_to_check.pop(0)  # remove one
    results = []
    for f in factors_to_check:
        table = groupcharactors(plaintext, f)
        for combination in generate_permutation(f):
            result = []
            arranged_table = swape_colume(table, combination)
            answer = return_to_text(arranged_table)
            scores = get_all_english_score_in_text(answer)
            score = get_english_score(answer)
            result.append(score)
            result.append(combination)
            outputfile.write(str(scores) + ", ")
            for c in combination:
                outputfile.write(str(c) + ", ")
            outputfile.write("\n")
            results.append(result)

    # Show results
    numbertop = 5

    topnumbers = []
    for i in range(numbertop):
        biggest = []
        for result in results:
            try:
                if result[0] > biggest[0]:
                    biggest = result
            except IndexError:
                biggest = result
        topnumbers.append(biggest)
        results.remove(biggest)
    print(topnumbers)
    for result in topnumbers:
        print(round(result[0], 2), end=', ')
        print(decrypt_transposition(text, result[1]))
    '''