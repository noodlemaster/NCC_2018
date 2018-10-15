import re
from src.checkenglishness import get_all_english_score_in_text, get_english_score
import enchant

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

def det_2x2(matrix):
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]
    det = a * d - b * c
    return det

def invert_2x2_undermod26(matrix, det):
    modulus_inverse = [[1, 1], [3, 9], [5, 21], [7, 15], [9, 3], [11, 19], [15, 7], [17, 23], [19, 11], [21, 5],
                       [23, 17], [25, 25]]
    det = det % 26
    for each in modulus_inverse:
        if each[0] == det:
            det_inverse = each[1]
        else:
            pass
    a = (((matrix[0][0]) % 26) * det_inverse) % 26
    b = (((matrix[0][1]) % 26) * det_inverse) % 26
    c = (((matrix[1][0]) % 26) * det_inverse) % 26
    d = (((matrix[1][1]) % 26) * det_inverse) % 26
    inv = [[d, b], [c, a]]
    return inv

def hill_check(det):
    if det != 0 and det % 2 != 0 and det % 13 != 0:
        return True
    else:
        return False

def is_english_word():
    dict = enchant.Dict("en_GB")
    return dict

def group_text(text, n):
    list_grouped = []
    PlainText = re.sub(r'\W', '', text)
    for i in range(0, len(PlainText), n):
        list_grouped.append(str.upper(PlainText[i:i + n]))
    return list_grouped

def matrix2text_2x1(twobyone):
    pos1, pos2 = twobyone[0][0], twobyone[1][0]
    alpha1, alpha2 = alphabet[pos1], alphabet[pos2]
    string = ''.join([alpha1, alpha2])
    return string

def text2matrix_2x2(list_grouped):
    matrix_list = []
    for each in list_grouped:
        if len(each) == 2:
            pos1, pos2 = alphabet.index(each[0]), alphabet.index(each[1])
            matrix = [[pos1], [pos2]]
            matrix_list.append(matrix)
        else:
            raise ValueError('This only works for 2x2 matrix. group_text(text, 2)')
    return matrix_list

def matrix_multiplication_2x2_2x1_undermod26(twobytwo, twobyone):
    a = twobytwo[0][0]
    b = twobytwo[0][1]
    c = twobytwo[1][0]
    d = twobytwo[1][1]
    e = twobyone[0][0]
    f = twobyone[1][0]
    g = (a * e + b * f) % 26
    h = (c * e + d * f) % 26
    matrix = [[g], [h]]
    return matrix

def generate_keys_2x2():
    possible_key = []
    for i in range(0, 25):
        for j in range(0, 25):
            for k in range(0, 25):
                for p in range(0, 25):
                    possible_keyword = alphabet[i] + alphabet[j] + alphabet[k] + alphabet[p]
                    if is_english_word().check(str.lower(possible_keyword)):
                        possible_matrix = [[i, j], [k, p]]
                        det = det_2x2(possible_matrix)
                        if hill_check(det):
                            inv = invert_2x2_undermod26(possible_matrix, det)
                            possible_key.append(inv)
                        else:
                            pass
                    else:
                        pass
    return possible_key

def hill_2x2(text):
    matrix_list = text2matrix_2x2(group_text(text, 2))
    possible_key = generate_keys_2x2()
    result_list = []
    for keys in possible_key:
        l = []
        for matrices in matrix_list:
            result = matrix_multiplication_2x2_2x1_undermod26(keys, matrices)
            string = matrix2text_2x1(result)
            l.append(string)
        char = ''.join(l)
        result_list.append(char)

    top_score = []
    for each in result_list:
        score = get_english_score(each)
        top_score.append(score)

    howmany = 5

    result = []
    for i in range(1, howmany):
        index = sorted(top_score)[-i]
        if isinstance(index, int):
            result.append([top_score[index], result_list[index]])
    for each in result:
        print(each)

if __name__ == '__main__':
    file = open('./questions/example/hill2x2.txt', 'r')
    text = file.read()
    file.close()
    # hill_2x2(text)
    # n = 2
    # print(group_text(text, n))
    # text2matrix_2x2(group_text(text, n))
    # print(textksplit(text, 6))
    # invert_2x2([[3, 2], [-1, 1]], 5)
    is_english_word()
    print(is_english_word().check('APPLE'))
