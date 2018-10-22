import itertools
from src.tools.checkenglishness import get_all_english_score_in_text, get_english_score

def get_factors(n):
    factors = []
    for i in range(n):
        if n%(i+1) == 0:
            factors.append(i + 1)
    return factors

def extract_alphabets(text):
    textnospace = []
    for c in text:
        if c.isalpha():
            textnospace.append(c.lower())
    return textnospace

def groupcharactors(text, n):
    table = []
    if len(text)%n != 0:
        return table
    row_n = int(len(text)/n)
    for r in range(row_n):
        row = []
        for c in range(n):
            row.append(text[c*row_n + r])
        table.append(row)
    return table

def swape_colume(table, conbination):
    newtable = []
    for row in table:
        newrow = []
        for n in conbination:
            newrow.append(row[n])
        newtable.append(newrow)
    return newtable

def return_to_text(table):
    text = ''
    for row in table:
        for c in row:
            text += c
    return text

def generate_permutation(num):
    return list(itertools.permutations(range(num)))

def organise_in_order_of_englishness(cvs):
    pass

def decrypt_transposition(text, combination):
    plaintext = extract_alphabets(text)
    table = groupcharactors(plaintext, len(combination))
    arranged_table = swape_colume(table, combination)
    answer = return_to_text(arranged_table)
    return answer

def decrypt_all_trasposition(text, max_columns = 7):
    outputfile = open('output.txt', 'w')
    plaintext = extract_alphabets(text)
    factors = get_factors(len(plaintext))
    factors_to_check = []
    for f in factors:
        if f > max_columns:
            break
        else:
            factors_to_check.append(f)
    factors_to_check.pop(0)  # remove one
    results = []
    for f in factors_to_check:
        table = groupcharactors(plaintext, f)
        for combination in generate_permutation(f):
            result = []
            arranged_table = swape_colume(table, combination)
            answer = return_to_text(arranged_table)
            scores = get_all_english_score_in_text(answer)
            score = get_english_score(answer)
            result.append(score)
            result.append(combination)
            outputfile.write(str(scores) + ", ")
            for c in combination:
                outputfile.write(str(c) + ", ")
            outputfile.write("\n")
            results.append(result)
    return results

def display_top_result(results, numbertop = 5):
    topnumbers = []
    for i in range(numbertop):
        biggest = []
        for result in results:
            try:
                if result[0] > biggest[0]:
                    biggest = result
            except IndexError:
                biggest = result
        topnumbers.append(biggest)
        results.remove(biggest)
    print(topnumbers)
    for result in topnumbers:
        print(round(result[0], 2), end=', ')
        print(decrypt_transposition(text, result[1]))

if __name__ == '__main__':
    #inputfile = open('../questions/example/transposition.txt', 'r')
    inputfile = open('../../questions/2017/6a.txt', 'r')
    text = inputfile.read()
    inputfile.close()

    display_top_result(decrypt_all_trasposition(text))