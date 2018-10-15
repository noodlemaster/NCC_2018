def get_all_words(file):
    return file.readlines()

def get_words_by_length(words, l):
    lwords = []
    for word in words:
        wordwithoutspace = ''
        for c in word:
            if c.isalpha():
                wordwithoutspace += c.lower()
        if len(wordwithoutspace) == l:
            lwords.append(wordwithoutspace)
    return lwords

def get_words_by_length_and_remove(words, l):
    lwords = []
    wordsleft = words.copy()
    for word in words:
        wordwithoutspace = ''
        for c in word:
            if c.isalpha():
                wordwithoutspace += c.lower()
            elif c == '\n':
                pass
            else:
                wordwithoutspace = ''
                break
        if len(wordwithoutspace) == l:
            lwords.append(wordwithoutspace)
            wordsleft.remove(word)
    return lwords, wordsleft

if __name__ == '__main__':
    # dictionary_file = open('./data/words/google-20000-english.txt', 'r')
    dictionary_file = open('./data/words/words_firefox.txt', 'r', errors='replace')
    words = get_all_words(dictionary_file)
    l = 1
    while True:
        # out_file = open('./data/words/length/google/' + str(l) + '.txt', 'w')
        out_file = open('./data/words/length/firefox/' + str(l) + '.txt', 'w')
        lwords, words = get_words_by_length_and_remove(words, l)
        for lword in lwords:
            out_file.write(lword + '\n')
        l += 1
        out_file.close()
        if len(words) == 0 or l > 40:
            print(words)
            break

