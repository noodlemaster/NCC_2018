import re

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

def get_frequency(text):
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