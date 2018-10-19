import re
from src.checkenglishness import get_english_score
from src.frequency import get_frequency, frequency_analysis

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def x_plus_a_check(index_e, index_t):
    if index_e > 4:
        a = 26 - (index_e - 4)
    else:
        a = 4 - index_e
    if (index_t + a) % 26 == 19:  # check with t
        return a
    else:
        return a #False

def get_map_of_x_plus_a(a):
    mapping = []
    for i in range(26):
        alphabet_position = (i + a) % 26
        mapping.append([alphabet[i], alphabet[alphabet_position]])  # [encrypt, decrypt]
    return mapping

def ax_plus_b_check(index_e, index_t):
    # [m, m']
    check = []
    modulus_inverse = [[1, 1], [3, 9], [5, 21], [7, 15], [9, 3], [11, 19], [15, 7], [17, 23], [19, 11], [21, 5],
                       [23, 17], [25, 25]]
    m = abs(index_e - index_t)
    for each in modulus_inverse:
        if each[0] == m:
            m_inverse = each[1]
            check.append(1)
        else:
            pass
    if len(check) == 1:
        if index_e > index_t:
            a = ((-15) * m_inverse) % 26
        else:
            a = (15 * m_inverse) % 26
        b = (4 - index_e * a) % 26
        return a, b
    else:
        return False, False

def get_map_of_ax_plus_b(a, b):
    mapping = []
    for i in range(0, 26):
        alphabet_position = (a * i + b) % 26
        mapping.append([alphabet[i], alphabet[alphabet_position]])  # [encrypt, decrypt]
    return mapping

def decrypt_mapping(text, mapping):
    text = text.upper()
    for each in mapping:
        old, new = each[0], str.lower(each[1])
        text = re.sub(old, new, text)
    return text


def decipher_by_english_check(text):
    # x+a
    # for a in range(26):
    #     # print(a, end='  ')
    #     result = []
    #     text_decrypted = decrypt_mapping(text, get_map_of_x_plus_a(a))
    #     # print(get_all_english_score_in_text(text_decrypted))
    #     score = get_english_score(text_decrypted)
    results = []
    # ax+b
    a_possible = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    for a in a_possible:
        for b in range(26):
            result = []
            text_decrypted = decrypt_mapping(text, get_map_of_ax_plus_b(a, b))
            score = get_english_score(text_decrypted)
            result.append(score)
            result.append([a, b])
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
        print("a=", end='')
        print(result[1][0], end=', ')
        print("b=", end='')
        print(result[1][1], end=', ')
        print(decrypt_mapping(text, get_map_of_ax_plus_b(result[1][0], result[1][1])))

def decipher_ax_plus_b_by_frequency(text):
    index_e, index_t = frequency_analysis(text)
    a, b = ax_plus_b_check(index_e, index_t)
    if a and b:
        text_decrypted = decrypt_mapping(text, get_map_of_ax_plus_b(a, b))
        return text_decrypted
    else:
        return False

def decipher_x_plus_a_by_frequency(text):
    index_e, index_t = frequency_analysis(text)
    a = x_plus_a_check(index_e, index_t)
    if not isinstance(a, bool):
        mapping = get_map_of_x_plus_a(a)
        text_decrypted = decrypt_mapping(text, mapping)
        return text_decrypted
    else:
        return False

if __name__ == '__main__':
    file = open('../questions/2017/3a.txt', 'r')
    text = file.read()
    file.close()

    #decipher_by_english_check(text)
    print(decipher_ax_plus_b_by_frequency(text))
    print(decipher_by_english_check(text))
    # for i in range(11):
    #     print(decrypt_mapping(text, get_map_of_x_plus_a(i)))