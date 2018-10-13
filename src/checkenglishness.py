bigrams = [["th", 1.52],["he", 1.28],["in", 0.94],["er", 0.94],["an", 0.82],["re", 0.68],["nd", 0.63],["at", 0.59],["on", 0.57],["nt", 0.56],["ha", 0.56],["es", 0.56],["st", 0.55],["en", 0.55],["ed", 0.53],["to", 0.52],["it", 0.50],["ou", 0.50],["ea", 0.47],["hi", 0.46],["is", 0.46],["or", 0.43],["ti", 0.34],["as", 0.33],["te", 0.27],["et", 0.19],["ng", 0.18],["of", 0.16],["al", 0.09],["de", 0.09],["se", 0.08],["le", 0.08],["sa", 0.06],["si", 0.05],["ar", 0.04],["ve", 0.04],["ra", 0.04],["ld", 0.02],["ur", 0.02]]
trigrams = [["THE", 1.87], ["AND", 0.78], ["ING", 0.69], ["HER", 0.42], ["THA", 0.37], ["ENT", 0.36], ["ERE", 0.33], ["ION", 0.33], ["ETH", 0.32], ["NTH", 0.32], ["HAT", 0.31], ["INT", 0.29], ["FOR", 0.28], ["ALL", 0.27], ["STH", 0.26], ["TER", 0.26], ["EST", 0.26], ["TIO", 0.26], ["HIS", 0.25], ["OFT", 0.24], ["HES", 0.24], ["ITH", 0.24], ["ERS", 0.24], ["ATI", 0.24], ["OTH", 0.23], ["FTH", 0.23], ["DTH", 0.23], ["VER", 0.22], ["TTH", 0.22], ["THI", 0.22], ["REA", 0.21], ["SAN", 0.21], ["WIT", 0.21], ["ATE", 0.2], ["ARE", 0.2], ["EAR", 0.19], ["RES", 0.19], ["ONT", 0.18], ["TIN", 0.18], ["ESS", 0.18], ["RTH", 0.18], ["WAS", 0.18], ["SOF", 0.18], ["EAN", 0.17], ["YOU", 0.17], ["SIN", 0.17], ["STO", 0.17], ["IST", 0.17], ["EDT", 0.16], ["EOF", 0.16], ["EVE", 0.16], ["ONE", 0.16], ["AST", 0.16], ["ONS", 0.16], ["DIN", 0.16], ["OME", 0.16], ["CON", 0.16], ["ERA", 0.16], ["STA", 0.15], ["OUR", 0.15], ["NCE", 0.15], ["TED", 0.15], ["GHT", 0.15], ["HEM", 0.15], ["MAN", 0.15], ["HEN", 0.15], ["NOT", 0.15], ["ORE", 0.15], ["OUT", 0.15], ["ORT", 0.15], ["ESA", 0.15], ["ERT", 0.15], ["SHE", 0.14], ["ANT", 0.14], ["NGT", 0.14], ["EDI", 0.14], ["ERI", 0.14], ["EIN", 0.14], ["NDT", 0.14], ["NTO", 0.14], ["ATT", 0.14], ["ECO", 0.13], ["AVE", 0.13], ["MEN", 0.13], ["HIN", 0.13], ["HEA", 0.13], ["IVE", 0.13], ["EDA", 0.13], ["INE", 0.13], ["RAN", 0.13], ["HEC", 0.13], ["TAN", 0.13], ["RIN", 0.13], ["ILL", 0.13], ["NDE", 0.13], ["THO", 0.13], ["HAN", 0.13], ["COM", 0.12], ["IGH", 0.12], ["AIN", 0.12]]

def removespace(text):
    textnospace = []
    for c in text:
        if c.isalpha():
            textnospace.append(c.lower())
    return textnospace

def countngram(text, n, list):
    bigram_count = [0] * len(list)
    for i in range(len(text)-n):
        chars = ''
        for k in range(n):
            chars += text[i + k]
        for j in range(len(list)):
            if chars == list[j][0].lower():
                bigram_count[j] += 1
    #percentage
    for i in range(len(list)):
        bigram_count[i] = bigram_count[i] / (len(text)-1) * 100

    return bigram_count

def checkenglishnes(percentage, data):
    score = 0.00000000000
    if len(data) != len(percentage):
        return score
    for i in range(len(data)):
        if percentage[i] > data[i][1]:
            score += 1
        else:
            # score += (percentage[i]/data[i][1])**2
            score += percentage[i]
    return score

def get_english_score_bigram(text):
    biscore = checkenglishnes(countngram(removespace(text), 2, bigrams), bigrams)
    return biscore

def get_english_score_trigram(text):
    triscore = checkenglishnes(countngram(removespace(text), 3, trigrams), trigrams)
    return triscore

def get_english_score(text):
    biscore = checkenglishnes(countngram(removespace(text), 2, bigrams), bigrams)
    triscore = checkenglishnes(countngram(removespace(text), 3, trigrams), trigrams)
    score = biscore * 2 + triscore * 5
    return score

def get_all_english_score_in_text(text):
    biscore = checkenglishnes(countngram(removespace(text), 2, bigrams), bigrams)
    triscore = checkenglishnes(countngram(removespace(text), 3, trigrams), trigrams)
    score = biscore * 2 + triscore * 5
    return str(round(score, 2)) + ", " + str(round(biscore, 2)) + ", " + str(round(triscore, 2))

if __name__ == '__main__':
    file = open('../questions/example/transposition_bbc.txt', 'r')
    text = file.read()
    file.close()
    print(get_english_score(text))