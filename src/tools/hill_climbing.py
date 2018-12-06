import random
import re
import math
from src.tools.checkenglishness import get_english_score

def alphabets():
    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
    return alphabets

def get_existing_letter(key):
    al = alphabets()
    l = list(set(list(key)))
    result = []
    for each in al:
        if each not in l:
            result.append(each)
    return result

def generate_random_keyword(lowerlimit, upperlimit, list):
    keyword = ''
    keyword_length = random.randint(lowerlimit, upperlimit)
    #print(keyword_length)
    while keyword_length > 0:
        char = random.choice(list)
        list.remove(char)
        keyword += char
        keyword_length -= 1
    return keyword

def generate_random_5x5grid(deleted_letter = 'I'):
    al = alphabets()
    al.remove(deleted_letter.upper())
    grid = []
    i = 5
    while i > 0:
        row = []
        string = generate_random_keyword(5, 5, al)
        for each in list(string):
            row.append(each)
        grid.append(row)
        i -= 1
    return grid

def random_5x5grid(grid):
    table = grid
    i = random.randint(1, 5)
    while i > 0:
        x1 = random.randint(0, 4)
        y1 = random.randint(0, 4)
        x2 = random.randint(0, 4)
        y2 = random.randint(0, 4)
        if x1 != x2 or y1 != y2:
            table[x1][y1], table[x2][y2] = table[x2][y2], table[x1][y1]
            #table[x2][y2] = table[x1][y1]
            i -= 1
    return table

def random_reverse_row_5x5(grid):
    i = random.randint(0, 4)
    row = grid[i]
    grid[i] = row[::-1]
    return grid

def random_reverse_column_5x5(grid):
    i = random.randint(0, 4)
    grid[0][i], grid[1][i], grid[3][i], grid[4][i] = grid[4][i], grid[3][i], grid[1][i], grid[0][i]
    return grid

def random_swapping(key):
    l = list(key)
    i, j = random.randint(0, len(l)-1), random.randint(0, len(l)-1)
    if i != j:
        pass
    else:
        i = (i + 1)%(len(key))
    l[i], l[j] = l[j], l[i]
    new_key = ''.join(l)
    return new_key

def reverse(key):
    k = key[::-1]
    return k

def random_substitution(key):
    l = list(key)
    i = random.randint(0, len(key)-2)
    target = random.choice(get_existing_letter(key))
    l[i] = target
    new_key = ''.join(l)
    return new_key

def random_substitution_n(key):
    i = random.randint(2, 4)
    while i > 0:
        key = random_substitution(key)
        i -= 1
    return key

def check_same_element_in2lists(l1, l2):
    for i in l1:
        for j in l2:
            if i == j:
                return False

def random_change_keyword_length(key):
    def add():
        i = random.randint(1, 25 - len(key))
        part = generate_random_keyword(1, i, get_existing_letter(key))
        l1 = list(set(list(part)))
        l = list(set(list(key)))
        for i in l1:
            for j in l:
                if i == j:
                    i = random.choice(get_existing_letter(key))
        return ''.join(l1)
    def minus():
        i = random.randint(4, len(key)-1)
        return i

    meth = ['add', 'minus']
    if len(key) < 5:
        return add() + key
    if len(key) > 20:
        return key[:minus()]
    else:
        method = random.choice(meth)
        if method == 'add':
            return add() + key
        else:
            j = minus()
            return key[:j]

def random_minor_change(type):
    if type == 'grid':
        methods = [random_reverse_row_5x5, random_reverse_column_5x5, random_5x5grid]
        meth = random.choices(methods, [0.25, 0.25, 0.5], k=1)
        return meth[0]
    else:
        methods = [reverse, random_substitution, random_change_keyword_length, random_substitution_n, random_swapping]
        meth = random.choices(methods, [0.2, 0.62, 0.7, 0.8, 0.2], k=1)
    # methods = [random_swapping, reverse, random_substitution]
    # meth = random.choices(methods, [0.20, 0.20, 0.60], k=1)
        return meth[0]

def table2str(table):
    if type(table) is str:
        return table
    else:
        s = ''
        for each in table:
            string = ''.join(each)
            s += string
        return s

def T_minus(t, count, STEP = 0.15):
    return t - STEP

def T_mutilier(t, count, multiplier = 0.95):
    return t*multiplier

def T_exp(t0, count, base = 0.95):
    return t0*(base**(count))

def T_exp2(t0, count, base = 3):
    return t0 * (base ** (-count))

def T_fast(t0, count):
    return t0/count

def T_boltz(t0, count):
    return t0/math.log(count)

def hill_climbing(text, config_dict):

    T = config_dict['T0']
    T_lowest = config_dict['T_lowest']
    NumberOfIterationPerT = config_dict['NumberOfIterationPerT']
    FunctionT = config_dict['FunctionT']
    CipherType = config_dict['CipherType']
    KeywordorGrid = config_dict['Keyword/Grid']
    LengthOfKey_lower = config_dict['LengthOfKey_lower']
    LengthOfKey_upper = config_dict['LengthOfKey_upper']
    Probability_threshold = config_dict['Probability_threshold']
    count = 1
    e = 2.71828182846

    PlainText = re.sub(r'\W', '', text)
    if KeywordorGrid == 'grid':
        parent_keyword = generate_random_5x5grid(deleted_letter = 'I')
    else:
        parent_keyword = generate_random_keyword(LengthOfKey_lower, LengthOfKey_upper, alphabets())
    parent_score = get_english_score(CipherType(PlainText, parent_keyword))
    #print(parent_score)
    highest_score = parent_score
    all_keys = []
    display_score = ''

    while T > T_lowest:
        print(count)
        countOfinter = 0

        while countOfinter <= NumberOfIterationPerT:
            meth = random_minor_change(KeywordorGrid)
            child_keyword = meth(parent_keyword)
            #print(child_keyword)
            if child_keyword not in all_keys:
                all_keys.append(table2str(child_keyword))
                resultText = CipherType(PlainText, child_keyword)
                child_score = get_english_score(resultText)
                dF = child_score - parent_score
                #print(child_score)
                if dF >= 0:
                    display_score = parent_score
                    parent_keyword = child_keyword
                    parent_score = child_score
                    if child_score > highest_score:
                        highest_score = child_score
                    print('#Iteration: ' + str(count) + '  Keyword: ' + table2str(parent_keyword) + '  Score: ' + str(child_score) + ' Highest score: ' + str(highest_score) + '  Parent score:  ' + str(display_score))
                else:
                    prob = e**(dF/T)
                    if prob > Probability_threshold:
                        parent_keyword = child_keyword
                        parent_score = child_score
                        print('#Iteration: ' + str(count) + '  Keyword: ' + table2str(parent_keyword) + '  Score: ' + str(parent_score) + '  Highest score: ' + str(highest_score) + '  Probability: ' + str(prob))
                    # else:
                    #     print('#Iteration: ' + str(count) + '  Unsuccessful' + '  Probability: ' + str(prob) + ' ' + str(T) + ' ' + str(dF))

                countOfinter += 1
                count += 1

        T = FunctionT(T, count)

if __name__ == '__main__':
    print(random_change_keyword_length('WKLDIPJFS'))
    #print(generate_random_keyword(6,18))
    #print(generate_random_5x5grid('I')[0][0])
    #print(alphabets())
    #print(random.randint(0,4))
    #print(random_5x5grid(generate_random_5x5grid()))
    l = [[1], [2]]
    print(l[0])
