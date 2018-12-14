from src.ciphers.affine import decrypt_mapping, get_map_of_ax_plus_b
from src.ciphers.text_replace import text_replace
from src.ciphers.transposition import generate_permutation, return_to_text, swape_colume
from src.ciphers.vigenere import decipher_vigenere, display_top_result
from src.tools.checkenglishness import get_all_english_score_in_text, get_english_score
from src.tools.display import show_frequency
from src.tools.frequency import get_possible_index_of_e_t_from_frequency
from src.tools.text_manipulation import text_split_in_order

# year = '2018'
# question = '10b_3'
# file = open('../../../questions/' + year + '/' + question + '.txt', 'r')
# original = file.read()
# file.close()

# results = decipher_vigenere(original, k=7, affine=True, use_a=False, display=True, reverse=False, auto=True)
# outputfile = open('output.txt', 'w')
# for result in results:
#     original = result[2]
    # table = text_split_in_order(original, 7)
    # # print(table[len(table)-1])
    # for i in range(4):
    #     table[len(table)-1].append('')
    #
    # for combination1 in generate_permutation(3):
    #     for combination2 in generate_permutation(4):
    #         combination = []
    #         for i in range(len(combination1)):
    #             combination.append(combination1[i])
    #         for i in range(len(combination2)):
    #             combination.append(combination2[i] + 3)
    #         arranged_table = swape_colume(table, combination)
    #         answer = return_to_text(arranged_table)
    #         output = str(get_english_score(answer)) + ', ' + str(combination) + ', ' + answer
    #         outputfile.write(output + "\n")
    #         print(output)
    # show_frequency(original, True, title=result[1])

number = -1
texts =[]
k = 7
if number == -1:
    for i in range(k):
        file = open('../../questions/2018/10b/10b_k_' + str(i) + '_a.txt', 'r')
        original = file.read()
        file.close()
        texts.append(original)
    length = 0
    for text in texts:
        length += len(text)
    original = ''
    for i in range(length):
        original += texts[(i % k)][int((i - (i % k)) / k)]
    print(original)
    file = open('../../questions/2018/10b/10b_working.txt', 'w')
    file.write(original)
    file.close()
    text_replace()
    # show_frequency(original, True, title='Added' + str(number))

elif number == -2:
    show_frequency(False, True, title='English')
    for i in range(k):
        file = open('../../questions/2018/10b/10b_k_' + str(i) + '.txt', 'r')
        original = file.read()
        file.close()
        print(original)
        show_frequency(original, True, title='original' + str(i))
else:
    show_frequency(False, True, title='English')
    file = open('../../questions/2018/10b/10b_k_' + str(number) + '.txt', 'r')
    original = file.read()
    file.close()
    print(original)
    show_frequency(original, True, title='original' + str(number))
# possible_indexes = get_possible_index_of_e_t_from_frequency(original, affine=True, e=3, t=8)
# for index in possible_indexes:
#     answer = decrypt_mapping(original, get_map_of_ax_plus_b(int(index[0][0]), int(index[0][1])))
#     show_frequency(answer, True, title=str(number) + str(index))

