import re

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

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

if __name__ == '__main__':
    file = open('../../questions/2017/6a.txt', 'r')
    text = file.read()
    file.close()
    frequency = get_frequency(text)
    for i in range(len(frequency)):
        print(alphabet[i] + ", " + str(frequency[i]))
    print("(e, t)")
    print(frequency_analysis(text))