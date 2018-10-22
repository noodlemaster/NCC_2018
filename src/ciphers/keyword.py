import re

from src.tools.checkenglishness import get_english_score
from src.tools.display import show_frequency

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
                    n = n % len(left_alpabets)
                map.append([alphabets[i].lower(), left_alpabets[n].upper()])
        maps.append(map)
    return maps

def get_map_with_keyword(keyword):
    keyword = extract_alphabets(keyword)
    last_c = keyword[len(keyword) - 1]
    index_c = alphabets.index(last_c.upper())
    alphabets_in_order = alphabets[index_c + 1:] + alphabets[:index_c]
    left_alpabets = []
    for c in alphabets_in_order:
        if keyword.lower().find(c.lower()) == -1:
            left_alpabets.append(c.lower())
    keyword_no_double = ""
    for k in keyword:
        if keyword_no_double.find(k.lower()) == -1:
            keyword_no_double += k.lower()
    map = []
    for i in range(26):
        if i < len(keyword_no_double):
            map.append([alphabets[i].lower(), keyword_no_double[i].upper()])
        else:
            n = i - len(keyword_no_double)
            if n >= len(left_alpabets):
                n = n % len(left_alpabets)
            map.append([alphabets[i].lower(), left_alpabets[n].upper()])
    return map

def check_all_with_keyword(text, keyword, index_e):
    maps = get_maps_with_keyword(keyword)
    results = []
    for map in maps:
        if index_e != -1:
            if map[4][1] != alphabets[index_e]:
                break
        original = decrypt_mapping(text, map)
        results.append([get_english_score(original), keyword, original])
    return results

def check_map_with_keyword(text, keyword, index_e = -1):
    map = get_map_with_keyword(keyword)
    if index_e != -1:
        if map[4][1] != alphabets[index_e]:
            return False
    original = decrypt_mapping(text, map)
    result = [get_english_score(original), keyword, original]
    return result

def try_all_keywords(text, start=4, end=10, index_e=-1, easy=False):
    results = []
    for i in range(start, end + 1):
        # file = open('../../../data/words/length/google/' + str(i) + '.txt', 'r')
        file = open('../../../data/words/length/firefox/' + str(i) + '.txt', 'r')
        words = file.readlines()
        file.close()
        for word in words:
            if easy:
                result = check_map_with_keyword(text, word, index_e)
                if result:
                    results.append(result)
                    results = keep_top_results(results, [], 100)
            else:
                result = check_all_with_keyword(text, word, index_e)
                results = keep_top_results(results, result, 100)
    return results

def keep_top_results(results, newresult, topnum=5):
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

def display_top_result(results, numbertop=5, easy=False):
    topnumbers = []
    for i in range(numbertop):
        biggest = []
        for result in results:
            try:
                if result[0] > biggest[0]:
                    biggest = result
            except IndexError:
                biggest = result
        try:
            results.remove(biggest)
            topnumbers.append(biggest)
        except:
            pass
    for result in topnumbers:
        if easy:
            print(round(result[0], 2), end=', ')
            print(result[1])
            print(result[2])
        else:
            print(round(result[0], 2), end=', ')
            print(result[1])
            print(result[2])

if __name__ == '__main__':
    file = open('../../../questions/2017/5a_2.txt', 'r')
    text = file.read()
    file.close()
    show_frequency(text, False)
    index_e_input = int(input('Input index of e'))
    display_top_result(try_all_keywords(text, 4, 8, index_e_input, True), 3, True)
    # display_top_result(check_all_with_keyword(text, 'deco'))
