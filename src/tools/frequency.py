import re

from src.tools.text_manipulation import removespace

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
bigrams = [["th", 1.52],["he", 1.28],["in", 0.94],["er", 0.94],["an", 0.82],["re", 0.68],["nd", 0.63],["at", 0.59],["on", 0.57],["nt", 0.56],["ha", 0.56],["es", 0.56],["st", 0.55],["en", 0.55],["ed", 0.53],["to", 0.52],["it", 0.50],["ou", 0.50],["ea", 0.47],["hi", 0.46],["is", 0.46],["or", 0.43],["ti", 0.34],["as", 0.33],["te", 0.27],["et", 0.19],["ng", 0.18],["of", 0.16],["al", 0.09],["de", 0.09],["se", 0.08],["le", 0.08],["sa", 0.06],["si", 0.05],["ar", 0.04],["ve", 0.04],["ra", 0.04],["ld", 0.02],["ur", 0.02]]
trigrams = [["THE", 1.87], ["AND", 0.78], ["ING", 0.69], ["HER", 0.42], ["THA", 0.37], ["ENT", 0.36], ["ERE", 0.33], ["ION", 0.33], ["ETH", 0.32], ["NTH", 0.32], ["HAT", 0.31], ["INT", 0.29], ["FOR", 0.28], ["ALL", 0.27], ["STH", 0.26], ["TER", 0.26], ["EST", 0.26], ["TIO", 0.26], ["HIS", 0.25], ["OFT", 0.24], ["HES", 0.24], ["ITH", 0.24], ["ERS", 0.24], ["ATI", 0.24], ["OTH", 0.23], ["FTH", 0.23], ["DTH", 0.23], ["VER", 0.22], ["TTH", 0.22], ["THI", 0.22], ["REA", 0.21], ["SAN", 0.21], ["WIT", 0.21], ["ATE", 0.2], ["ARE", 0.2], ["EAR", 0.19], ["RES", 0.19], ["ONT", 0.18], ["TIN", 0.18], ["ESS", 0.18], ["RTH", 0.18], ["WAS", 0.18], ["SOF", 0.18], ["EAN", 0.17], ["YOU", 0.17], ["SIN", 0.17], ["STO", 0.17], ["IST", 0.17], ["EDT", 0.16], ["EOF", 0.16], ["EVE", 0.16], ["ONE", 0.16], ["AST", 0.16], ["ONS", 0.16], ["DIN", 0.16], ["OME", 0.16], ["CON", 0.16], ["ERA", 0.16], ["STA", 0.15], ["OUR", 0.15], ["NCE", 0.15], ["TED", 0.15], ["GHT", 0.15], ["HEM", 0.15], ["MAN", 0.15], ["HEN", 0.15], ["NOT", 0.15], ["ORE", 0.15], ["OUT", 0.15], ["ORT", 0.15], ["ESA", 0.15], ["ERT", 0.15], ["SHE", 0.14], ["ANT", 0.14], ["NGT", 0.14], ["EDI", 0.14], ["ERI", 0.14], ["EIN", 0.14], ["NDT", 0.14], ["NTO", 0.14], ["ATT", 0.14], ["ECO", 0.13], ["AVE", 0.13], ["MEN", 0.13], ["HIN", 0.13], ["HEA", 0.13], ["IVE", 0.13], ["EDA", 0.13], ["INE", 0.13], ["RAN", 0.13], ["HEC", 0.13], ["TAN", 0.13], ["RIN", 0.13], ["ILL", 0.13], ["NDE", 0.13], ["THO", 0.13], ["HAN", 0.13], ["COM", 0.12], ["IGH", 0.12], ["AIN", 0.12]]

# def get_frequency(text):
#     freq_character = []
#     # text = extract_text()
#     for j in alphabet:
#         result = re.findall(j, text)
#         freq_character.append(len(result))
#     probability = []
#     PlainText = re.sub(r'\W', '', text)
#     total_cahracter = len(PlainText)
#     for each in freq_character:
#         probability.append(int(each) / total_cahracter)
#     #print(probability)
#     return probability

def x_plus_a_check(index_e, index_t = -1):
    if index_e > 4:
        a = 26 - (index_e - 4)
    else:
        a = 4 - index_e
    if index_t == -1:
        return a
    if (index_t + a) % 26 == 19:  # check with t
        return a
    else:
        return False

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

def count_alphabet(text, alphabet):
    alphabet_count = [0] * len(alphabet)
    for i in range(len(alphabet)):
        for c in text:
            if c.lower() == alphabet[i].lower():
                alphabet_count[i] += 1
    return alphabet_count

def get_frequency(text):
    counts = count_alphabet(text, alphabet)
    probability = []
    total = 0
    for count in counts:
        total += count
    for count in counts:
        probability.append(count / total)
    return probability

def frequency_analysis(text):
    probability = get_frequency(text.lower())
    maximum_e = max(probability)
    maximum_t = sorted(probability)[-2]
    index_e = -1
    index_t = -1
    if abs(maximum_e - 0.12702) <= 0.18:
        index_e = probability.index(maximum_e)
    if abs(maximum_t - 0.09056) <= 0.15:
        index_t = probability.index(maximum_t)
    return index_e, index_t

def sort_function(l):
  return l[1]

def get_possible_index_of_e_t_from_frequency(text, affine=False, e=3, t=4):
    probability = get_frequency(text.lower())
    sorted_probability = []
    for i in range(len(probability)):
        sorted_probability.append([i, probability[i]])
    sorted_probability.sort(reverse=True, key=sort_function)
    results = []
    for i in range(e):
        index_e = sorted_probability[i][0]
        for j in range(t+1):
            if i != j:
                index_t = sorted_probability[j][0]
                indexes = [index_e, index_t]
                results.append(indexes)
    possible_conbination = []
    for result in results:
        if affine:
            a, b = ax_plus_b_check(result[0], result[1])
            if not isinstance(a, bool):
                possible_conbination.append([[a, b], result])
        else:
            a = x_plus_a_check(result[0], result[1])
            if not isinstance(a, bool):
                possible_conbination.append([a, result])
    return possible_conbination

def get_all_n_gram(text, n):
    all_n_gram_list = []
    for i in range(len(text)-n):
        chars = ''
        for k in range(n):
            chars += text[i + k]
        for j in range(len(all_n_gram_list)):
            if chars == all_n_gram_list[j][0]:
                all_n_gram_list[j][1] += 1
                chars = ''
                break
        if not chars == '':
            all_n_gram_list.append([chars, 1])
    all_n_gram_list.sort(reverse=True, key=sort_function)
    return all_n_gram_list

def get_n_gram_frequency(text, n):
    text = removespace(text)
    all_n_gram_list = get_all_n_gram(text, n)
    n_gram_frequency = []
    length = len(text)-n
    for l in all_n_gram_list:
        n_gram_frequency.append([l[0].upper(), l[1]/length*100])
    return n_gram_frequency

if __name__ == '__main__':
    file = open('../../questions/2018/5b_a.txt', 'r')
    text = file.read()
    file.close()
    # frequency = get_frequency(text)
    # for i in range(len(frequency)):
    #     print(alphabet[i] + ", " + str(frequency[i]))
    # print("(e, t)")
    # print(frequency_analysis(text))
    get_n_gram_frequency(text, 1)