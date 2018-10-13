import re
from checkenglishness import get_all_english_score_in_text

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
    file = open('questions/2018/1a.txt', 'r')
    text = file.read()
    file.close()
    #x+a
    for a in range(26):
        print(a, end='  ')
        text_decrypted = decrypt_mapping(text, get_map_of_x_plus_a(a))
        print(get_all_english_score_in_text(text_decrypted))


    # #ax+b
    # a_possible = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    # for a in a_possible:
    #     for b in range(26):
    #         text_decrypted = decrypt_mapping(text, get_map_of_ax_plus_b(a, b))
    #         score = get_english_score(text_decrypted)
    #         print(score)
