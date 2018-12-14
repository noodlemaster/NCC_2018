from src.ciphers.affine import decrypt_mapping, get_map_of_ax_plus_b
from src.ciphers.vigenere import decipher_vigenere, display_top_result, decipher_vigenere_with_a
from src.tools.checkenglishness import get_english_score
from src.tools.text_manipulation import removespace

file = open('../../../questions/2017/6b.txt', 'r')
text = file.read()
file.close()
original_text = ''.join(removespace(text))
# print(original_text)
# newtext = decrypt_mapping(original_text, get_map_of_ax_plus_b(15, 0))
# print(newtext)
#                                             [0, 14, 5, 10, 22, 24, 17, 11, 4,  0, 24, 17, 1, 18, 2]
# newtext = decipher_vigenere_with_a(newtext, [0, 14, 5, 10, 22, 24, 17,  0, 18, 2, 24,  5, 1, 18, 2])[2]
# # display_top_result(decipher_vigenere(newtext, k=15, affine=False, use_a=False, display=True, reverse=False, auto=False))
# print(get_english_score(newtext))
# print(newtext)

a_possible = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
# a_possible = [15]
for a in a_possible:
    print(a)
    newtext = decrypt_mapping(original_text, get_map_of_ax_plus_b(a, 0))
    display_top_result(decipher_vigenere(newtext, k=7, affine=False, use_a=False, display=True, reverse=False, auto=True))
    print(newtext)
