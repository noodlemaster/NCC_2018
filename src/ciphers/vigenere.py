import math
from src.ciphers.affine import decipher_x_plus_a_by_frequency, x_plus_a_check, get_map_of_x_plus_a, decrypt_mapping
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

def calculate_ioc(text):
def decipher_vigenere(text, k = -1):
    if k == -1:
        show_ioc(text, 26)
        k = int(input('Input the keyword length. k='))
    list_texts = textksplit(extract_alphabets(text), k)
    while True:
        deciphered_texts = []
        for list_text in list_texts:
            list_text_string = ''.join(list_text)
            index_e, index_t = frequency_analysis(''.join(list_text_string))
            a = x_plus_a_check(index_e, index_t)
            print(index_e, end=', ')
            print(index_t, end=', ')
            print(a)
            show_frequency(list_text_string, False)
            index_e_input = int(input('Input index of e (-1 to agree, -2 to leave)'))
            if index_e_input == -1:
                answer = decipher_x_plus_a_by_frequency(list_text_string)
            elif index_e_input == -2:
                answer = ''
                for i in range(len(list_text_string)):
                    answer += '_'
            else:
                print(index_e_input)
                answer = decrypt_mapping(list_text_string, get_map_of_x_plus_a(x_plus_a_check(index_e_input, -1)))
            deciphered_texts.append(answer)

        length = 0
        for deciphered_text in deciphered_texts:
            length += len(deciphered_text)
        answer = ""
        for i in range(length):
            answer += deciphered_texts[(i%k)][int((i-(i%k))/k)]

        print(answer)
        if int(input('1 to finish')) == 1:
            break
    return answer

if __name__ == '__main__':
    #file = open('../../questions/example/vigenere.txt', 'r')
    file = open('../../questions/2017/4b.txt', 'r')
    text = file.read()
    file.close()
    decipher_vigenere(text)