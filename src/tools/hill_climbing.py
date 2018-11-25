import random
import re
import math
from src.tools.checkenglishness import get_english_score

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']

def generate_random_keyword(lowerlimit, upperlimit):
    keyword = ''
    keyword_length = random.randint(lowerlimit, upperlimit)
    #print(keyword_length)
    while keyword_length > 0:
        char = random.choice(alphabets)
        keyword += char
        keyword_length -= 1
    return keyword

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
    key = key[::-1]
    return key

def random_substitution(key):
    l = list(key)
    i = random.randint(0, len(key)-1)
    target = random.choice(alphabets)
    if l[i] != target:
        l[i] = target
    else:
        i  = (i + 1)%(len(key))
        l[i] = target
    new_key = ''.join(l)
    return new_key

def random_change_keyword_length(key):
    def add():
        i = random.randint(1, 25 - len(key))
        part = generate_random_keyword(1, i)
        l1 = list(part)
        l2 = list(set(list(key)))
        for i in l1:
            for j in l2:
                if i == j:
                    i = alphabets[random.randint(0, 25)]
        return ''.join(l1)
    def minus():
        i = random.randint(1, len(key)-1)
        return i

    meth = ['add', 'minus']
    if len(key) < 4:
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

def random_minor_change():
    methods = [random_swapping, reverse, random_substitution, random_change_keyword_length]
    meth = random.choices(methods, [0.2, 0.1, 0.40, 0.3], k=1)
    # methods = [random_swapping, reverse, random_substitution]
    # meth = random.choices(methods, [0.20, 0.20, 0.60], k=1)
    return meth[0]

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
    LengthOfKey_lower = config_dict['LengthOfKey_lower']
    LengthOfKey_upper = config_dict['LengthOfKey_upper']
    Probability_threshold = config_dict['Probability_threshold']
    count = 1
    e = 2.71828182846

    PlainText = re.sub(r'\W', '', text)
    parent_keyword = generate_random_keyword(LengthOfKey_lower, LengthOfKey_upper)
    parent_score = get_english_score(CipherType(PlainText, parent_keyword))
    #print(parent_score)
    highest_score = parent_score

    while T > T_lowest:
        countOfinter = 0

        while countOfinter <= NumberOfIterationPerT:
            meth = random_minor_change()
            child_keyword = meth(parent_keyword)
            resultText = CipherType(PlainText, child_keyword)
            child_score = get_english_score(resultText)
            dF = child_score - parent_score
            #print(child_score)
            if dF > 0:
                parent_keyword = child_keyword
                parent_score = child_score
                if child_score > highest_score:
                    highest_score = child_score
                print('#Iteration: ' + str(count) + '  Keyword: ' + parent_keyword + '  Score: ' + str(child_score) + ' Highest score: ' + str(highest_score))
            else:
                prob = e**(dF/T)
                if prob > Probability_threshold:
                    parent_keyword = child_keyword
                    parent_score = child_score
                    print('#Iteration: ' + str(count) + '  Keyword: ' + parent_keyword + '  Score: ' + str(parent_score) + '  Highest score: ' + str(highest_score) + '  Probability: ' + str(prob))
                # else:
                #     print('#Iteration: ' + str(count) + '  Unsuccessful' + '  Probability: ' + str(prob) + ' ' + str(T) + ' ' + str(dF))

            count += 1
            countOfinter += 1
        T = FunctionT(T, count)
