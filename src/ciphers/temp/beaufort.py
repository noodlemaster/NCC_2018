import math

from src.ciphers.affine import decrypt_mapping
from src.ciphers.vigenere import choose_k_from_ioc, extract_alphabets, textksplit
from src.tools.display import show_frequency

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def get_map_of_reverse_x_plus_a(a):
    mapping = []
    for i in range(0, 26):
        alphabet_position = (a - i) % 26
        mapping.append([alphabet[alphabet_position], alphabet[i]])  # [encrypt, decrypt]
    return mapping

def get_map_of_reverse_x_plus_a_from_index_e(index_e):
    mapping = []
    for a in range(0,26):
        for i in range(0, 26):
            alphabet_position = (a - i) % 26
            mapping.append([alphabet[alphabet_position], alphabet[i]])  # [encrypt, decrypt]
    if mapping[index_e][1] == 'E':
        return mapping
    else:
        return False

def decipher_beaufort_with_keyword(text, key):
    k = len(key)
    list_texts = textksplit(extract_alphabets(text), k)
    deciphered_texts = []
    for i in range(len(list_texts)):
        list_text_string = ''.join(list_texts[i])
        answer = decrypt_mapping(list_text_string, get_map_of_reverse_x_plus_a(key[i]))
        deciphered_texts.append(answer)
    length = 0
    for deciphered_text in deciphered_texts:
        length += len(deciphered_text)
    answer = ''
    for i in range(length):
        answer += deciphered_texts[(i % k)][int((i - (i % k)) / k)]
    return answer

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

def decipher_beaufort(text, k = -1):
    if k == -1:
        k = choose_k_from_ioc(text)
    a_for_each = choose_possible_as_by_frequency(text, k)
    # results = decipher_vigenere_all_possible_combination_of_a(text, k, a_for_each)
    return results

if __name__ == '__main__':
    file = open('../../../questions/2017/5b.txt', 'r')
    text = file.read()
    file.close()
    print(decipher_beaufort_with_keyword(text, [0,17,2,0,13,0,8,12,15,4,17,8,8]))
    # display_top_result(decipher_vigenere(text))