import math

import time

from src.ciphers.affine import decipher_x_plus_a_by_frequency, x_plus_a_check, get_map_of_x_plus_a, decrypt_mapping, \
    ax_plus_b_check, get_map_of_ax_plus_b
from src.tools.checkenglishness import get_english_score
from src.tools.display import show_ioc, show_frequency
from src.tools.frequency import frequency_analysis, get_possible_index_of_e_t_from_frequency
from src.tools.text_manipulation import reverse_text, removespace

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

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
        for i in range(math.ceil(len(text) / k)):
            try:
                chars.append(text[i * k + r])
            except IndexError:
                pass
        listofchars.append(chars)
    return listofchars

def gen_permination(lists):
    answers = []
    if len(lists) > 1:
        last = gen_permination(lists[1:])
        for i in lists[0]:
            for l in last:
                if isinstance(l, list):
                    answer = [i] + l
                else:
                    answer = [i] + [l]
                answers.append(answer)
        return answers
    elif len(lists) == 1:
        return lists[0]

def choose_k_from_ioc(text, showk=26):
    show_ioc(text, showk)
    k = int(input('Input the keyword length. k='))
    return k

def choose_possible_as_by_frequency(text, k, affine, use_a=False, display=True, auto=False):
    list_texts = textksplit(extract_alphabets(text), k)
    a_for_each = []
    for list_text in list_texts:
        list_text_string = ''.join(list_text)
        if affine:
            possible_indexes = get_possible_index_of_e_t_from_frequency(''.join(list_text_string), affine=True, e=3,
                                                                        t=4)
            print(possible_indexes)
        else:
            possible_indexes = get_possible_index_of_e_t_from_frequency(''.join(list_text_string), e=5, t=10)
            print(possible_indexes)
        if auto:
            a_s = []
            if len(possible_indexes) == 0:
                if affine:
                    a_s.append([int(1), int(0)])
                else:
                    a_s.append(0)
            for index in possible_indexes:
                if affine:
                    a_s.append([int(index[0][0]), int(index[0][1])])
                else:
                    a_s.append(int(index[0]))
        else:
            if display:
                show_frequency(list_text_string, False)
            if not use_a:
                index_e_input = input('Input possible indexes of e (split them using \',\' )(-1 to agree)')
                indexes = index_e_input.split(',')
                a_s = []
                if int(indexes[0]) == -1:
                    for index in possible_indexes:
                        a_s.append(int(index[0]))
                else:
                    for index in indexes:
                        a_s.append(x_plus_a_check(int(index)))
            else:
                index_e_input = input('Input possible a (split them using \',\' )')
                indexes = index_e_input.split(',')
                a_s = []
                if int(indexes[0]) == -1:
                    for index in possible_indexes:
                        a_s.append(int(index[0]))
                else:
                    for index in indexes:
                        a_s.append((int(index)))
        a_for_each.append(a_s)
    return (a_for_each)

def decipher_vigenere_all_possible_combination_of_a(text, k, a_for_each, affine=False, reverse=False):
    list_texts = textksplit(extract_alphabets(text), k)
    all_combinations_of_a = gen_permination(a_for_each)
    answers = []
    print(len(all_combinations_of_a))
    for a_s in all_combinations_of_a:
        deciphered_texts = []
        first = True
        for i in range(len(list_texts)):
            list_text_string = ''.join(list_texts[i])
            if affine:
                if first:
                    add = [a_s[len(a_s) - 2], a_s[len(a_s)-1]]
                    a_s = a_s[0:len(a_s) - 2]
                    a_s.append(add)
                    first =False
                answer = decrypt_mapping(list_text_string, get_map_of_ax_plus_b(int(a_s[i][0]), int(a_s[i][1])))
            else:
                answer = decrypt_mapping(list_text_string, get_map_of_x_plus_a(a_s[i]))
            deciphered_texts.append(answer)
        length = 0
        for deciphered_text in deciphered_texts:
            length += len(deciphered_text)
        answer = ''
        for i in range(length):
            answer += deciphered_texts[(i % k)][int((i - (i % k)) / k)]
        if not reverse:
            answers.append([get_english_score(answer), a_s, answer])
        elif reverse:
            reversed_text = reverse_text(answer)
            answers.append([get_english_score(reversed_text), a_s, reversed_text])
    return answers

def decipher_vigenere_with_a(text, a_s):
    k = len(a_s)
    list_texts = textksplit(extract_alphabets(text), k)
    deciphered_texts = []
    for i in range(len(list_texts)):
        list_text_string = ''.join(list_texts[i])
        answer = decrypt_mapping(list_text_string, get_map_of_x_plus_a(a_s[i]))
        deciphered_texts.append(answer)
    length = 0
    for deciphered_text in deciphered_texts:
        length += len(deciphered_text)
    answer = ''
    for i in range(length):
        answer += deciphered_texts[(i % k)][int((i - (i % k)) / k)]
    answer = [get_english_score(answer), a_s, answer]
    return answer

def decipher_vigenere(text, affine=False, k=-1, showk=26, use_a=False, display=True, reverse=False, auto=False):
    if k == -1:
        k = choose_k_from_ioc(text, showk)
    a_for_each = choose_possible_as_by_frequency(text, k, affine, use_a, display, auto)
    print(a_for_each)
    start = time.time()
    results = decipher_vigenere_all_possible_combination_of_a(text, k, a_for_each, affine=affine, reverse=reverse)
    print(time.time() - start)
    return results

def display_top_result(results, numbertop=20):
    topnumbers = []
    for i in range(numbertop):
        biggest = []
        for result in results:
            try:
                if result[0] > biggest[0]:
                    biggest = result
            except IndexError:
                biggest = result
        try:
            results.remove(biggest)
            topnumbers.append(biggest)
        except:
            pass
    for result in topnumbers:
        print(round(result[0], 2), end=', ')
        print(result[1])
        print(result[2])

if __name__ == '__main__':
    year = '2018'
    question = '10b_3'
    file = open('../../questions/' + year + '/' + question + '.txt', 'r')
    text = file.read()
    file.close()
    # display_top_result(decipher_vigenere(text, k = 7, affine=True, use_a=False, display=True, reverse=False, auto=True))
    # display_top_result(decipher_vigenere(text, k=7, affine=True, use_a=False, display=True, reverse=False, auto=True))
    texts = textksplit(extract_alphabets(text), 7)
    for i in range(len(texts)):
        outputfile = open('../../questions/2018/10b/10b_k_' + str(i) + '_a.txt', 'w')
        for cs in texts[i]:
            for c in cs:
                outputfile.write(c.upper())
                # outputfile.write(',')
            outputfile.write('\n')
        outputfile.close()