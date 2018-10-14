import re

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

def frequency(text):
    freq_character = []
    # text = extract_text()
    for j in alphabet:
        result = re.findall(j, text)
        freq_character.append(len(result))
    probability = []
    PlainText = re.sub(r'\W', '', text)
    total_cahracter = len(PlainText)
    for each in freq_character:
        probability.append(int(each) / total_cahracter)
    #print(probability)
    return probability

def count_alphabet(text, alphabet):
    alphabet_count = [0] * len(alphabet)
    for i in range(len(alphabet)):
        for c in text:
            if c == alphabet[i].lower():
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
    letter_freq = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094,
                   0.00153, 0.0772, 0.04025, 0.02406, 0.06749, 0.07507, 0.01925, 0.0095,
                   0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.0236, 0.0015, 0.01974, 0.00074]
    maximum_e = max(probability)
    maximum_t = sorted(probability)[-2]
    index_e = -1
    index_t = -1
    if abs(maximum_e - 0.12702) <= 0.18:
        index_e = probability.index(maximum_e)
    if abs(maximum_t - 0.09056) <= 0.15:
        index_t = probability.index(maximum_t)
    return index_e, index_t

if __name__ == '__main__':
    text = 'XSFJD JMNRF RUDJV LMYFT GWWHP T'
    #frequency(text)
    frequency_analysis(text)