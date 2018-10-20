import re

from src.tools.checkenglishness import get_english_score

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
def extract_alphabets(text):
    textnospace = ''
    for c in text:
        if c.isalpha():
            textnospace += c.lower()
    return textnospace

def decrypt_mapping(text, mapping):
    text = text.upper()
    for each in mapping:
        old, new = each[1], str.lower(each[0])
        text = re.sub(old, new, text)
    return text

def get_maps_with_keyword(keyword):
    maps = []
    keyword = extract_alphabets(keyword)
    left_alpabets = []
    for c in alphabets:
        if keyword.lower().find(c.lower()) == -1:
            left_alpabets.append(c.lower())
    keyword_no_double = ""
    for k in keyword:
        if keyword_no_double.find(k.lower()) == -1:
            keyword_no_double += k.lower()
    for p in range(len(left_alpabets)):
        map = []
        for i in range(26):
            if i < len(keyword_no_double):
                map.append([alphabets[i].lower(), keyword_no_double[i].upper()])
            else:
                n = i - len(keyword_no_double) + p
                if n >= len(left_alpabets):
                    n = n%len(left_alpabets)
                map.append([alphabets[i].lower(), left_alpabets[n].upper()])
        maps.append(map)
    return maps

def check_all_with_keyword(text, keyword):
    maps = get_maps_with_keyword(keyword)
    results = []
    for map in maps:
        original = decrypt_mapping(text, map)
        results.append([get_english_score(original), keyword, original])
    return results

def try_all_keywords(text, start = 4, end = 10):
    results = []
    for i in range(start, end + 1):
        file = open('../../../data/words/length/google/' + str(i) + '.txt', 'r')
        words = file.readlines()
        file.close()
        for word in words:
            result = check_all_with_keyword(text, word)
            results = keep_top_results(results, result, 100)
    return results


def keep_top_results(results, newresult, topnum = 5):
    all_results = results + newresult
    top_result = []
    if topnum > len(all_results):
        topnum = len(all_results)
    for i in range(topnum):
        biggest = []
        for result in all_results:
            try:
                if result[0] > biggest[0]:
                    biggest = result
            except IndexError:
                biggest = result
        top_result.append(biggest)
        all_results.remove(biggest)
    return top_result

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
    for result in topnumbers:
        print(round(result[0], 2), end=', ')
        print(result[1])
        print(result[2])

if __name__ == '__main__':
    file = open('../../../questions/2017/5a.txt', 'r')
    text = file.read()
    file.close()
    display_top_result(try_all_keywords(text, 4, 4), 10)
    # display_top_result(check_all_with_keyword(text, 'deco'))