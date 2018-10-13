import re
from src.checkenglishness import get_english_score

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def get_map_of_x_plus_a(a):
    mapping = []
    for i in range(26):
        alphabet_position = (i + a) % 26
        mapping.append([alphabet[i], alphabet[alphabet_position]])  # [encrypt, decrypt]
    return mapping

def get_map_of_ax_plus_b(a, b):
    mapping = []
    for i in range(0, 26):
        alphabet_position = (a * i + b) % 26
        mapping.append([alphabet[i], alphabet[alphabet_position]])  # [encrypt, decrypt]
    return mapping

def decrypt_mapping(text, mapping):
    for each in mapping:
        old, new = each[0], str.lower(each[1])
        text = re.sub(old, new, text)
    return text

if __name__ == '__main__':
    file = open('../questions/2017/5a.txt', 'r')
    text = file.read()
    file.close()
    #x+a
    # for a in range(26):
    #     # print(a, end='  ')
    #     result = []
    #     text_decrypted = decrypt_mapping(text, get_map_of_x_plus_a(a))
    #     # print(get_all_english_score_in_text(text_decrypted))
    #     score = get_english_score(text_decrypted)
    results = []
    #ax+b
    a_possible = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    for a in a_possible:
        for b in range(26):
            result = []
            text_decrypted = decrypt_mapping(text, get_map_of_ax_plus_b(a, b))
            score = get_english_score(text_decrypted)
            result.append(score)
            result.append([a, b])
            results.append(result)

    #Show results
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