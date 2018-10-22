import math
from src.ciphers.affine import decipher_x_plus_a_by_frequency, x_plus_a_check, get_map_of_x_plus_a, decrypt_mapping
from src.tools.checkenglishness import get_english_score
from src.tools.display import show_ioc, show_frequency
from src.tools.frequency import frequency_analysis

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

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
        for i in range(math.ceil(len(text)/k)):
            try:
                chars.append(text[i*k+r])
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

def choose_k_from_ioc(text):
    show_ioc(text, 26)
    k = int(input('Input the keyword length. k='))
    return k

def choose_possible_as_by_frequency(text, k):
    list_texts = textksplit(extract_alphabets(text), k)
    a_for_each = []
    for list_text in list_texts:
        list_text_string = ''.join(list_text)
        index_e, index_t = frequency_analysis(''.join(list_text_string))
        a = x_plus_a_check(index_e, index_t)
        print(index_e, end=', ')
        print(index_t, end=', ')
        print(a)
        show_frequency(list_text_string, False)
        index_e_input = input('Input possible indexes of e (split them using \',\' )')
        indexes = index_e_input.split(',')
        a_s = []
        for index in indexes:
            a_s.append(x_plus_a_check(int(index)))
        a_for_each.append(a_s)
    return (a_for_each)

def decipher_vigenere_all_possible_combination_of_a(text, k, a_for_each):
    list_texts = textksplit(extract_alphabets(text), k)
    all_combinations_of_a = gen_permination(a_for_each)
    answers = []
    print(len(all_combinations_of_a))
    for a_s in all_combinations_of_a:
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
        answers.append([get_english_score(answer), a_s, answer])
    return answers

def decipher_vigenere(text, k = -1):
    if k == -1:
        k = choose_k_from_ioc(text)
    a_for_each = choose_possible_as_by_frequency(text, k)
    results = decipher_vigenere_all_possible_combination_of_a(text, k, a_for_each)
    return results

def display_top_result(results, numbertop=5):
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
    # file = open('../../questions/example/vigenere.txt', 'r')
    file = open('../../questions/2017/5b.txt', 'r')
    text = file.read()
    file.close()
    display_top_result(decipher_vigenere(text))