from matplotlib import pyplot

from src.tools.frequency import get_frequency, get_n_gram_frequency
from src.tools.index_of_coincidence import get_average_ioc_from_1_to_k, get_first_ioc_from_1_to_k
from src.tools.text_manipulation import reverse_text, extract_alphabets, removespace, text_split_in_order

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

def show_frequency(text, alp = True, title=''):
    if text:
        frequency = get_frequency(text)
    else:
        file = open('../../data/letter_frequency.txt', 'r')
        frequency = file.readlines()
        file.close()
        for i in range(len(frequency)):
            frequency[i] = float(frequency[i].strip())/100
    pyplot.title('Character frequency ' + str(title))
    list = []
    list_s = []
    for i in range(26):
        list.append(i)
    if alp:
        if text:
            pyplot.bar(list, frequency, tick_label=alphabet)
        else:
            lower_alpha = []
            for a in alphabet:
                lower_alpha.append(a.lower())
            pyplot.bar(list, frequency, tick_label=lower_alpha)
    else:
        pyplot.bar(list, frequency, tick_label=list)
    pyplot.hlines(0.12702, 0, 27)
    pyplot.hlines(0.09056, 0, 27)
    pyplot.show()

def show_ioc(text , n, average = True):
    if average:
        iocs = get_average_ioc_from_1_to_k(text, n)
    else:
        iocs = get_first_ioc_from_1_to_k(text, n)
    pyplot.title('IOCs')
    list = []
    for i in range(n):
        list.append(i+1)
    pyplot.bar(list, iocs, tick_label=list)
    pyplot.hlines(0.0667, 0, n + 1)
    pyplot.show()

def show_n_gram_frequency(text, n, top=10):
    if text:
        frequency = get_n_gram_frequency(text, n)
        frequency = frequency[0:top]
    else:
        file = open('../../data/' + str(n) + '_gram_frequency.txt', 'r')
        frequency_raw = file.readlines()
        file.close()
        frequency = []
        for i in range(top):
            frequency.append([frequency_raw[i][2:2+n].lower(), float(frequency_raw[i][5+n:9+n])])
    name_plot = []
    data_plot = []
    num_list = []
    for i in range(len(frequency)):
        num_list.append(i+1)
    for f in frequency:
        name_plot.append(f[0])
        data_plot.append(f[1])
    pyplot.title(str(n) + ' gram frequency')
    pyplot.barh(num_list, data_plot)
    pyplot.yticks(num_list, name_plot)
    pyplot.gca().invert_yaxis()
    pyplot.show()

def check_two_same_letters(text):
    text = ''.join(extract_alphabets(removespace(text)))
    for a in alphabet:
        num = text.find(a.lower() + a.lower())
        if num != -1:
            if num % 2 == 1:
                print(a + a + ' False')
            else:
                print(a + a + ' True')
    print('done')

def two_letters_frequency(text):
    text = ''.join(extract_alphabets(removespace(text)))
    text_split_in_order(text, 2)


if __name__ == '__main__':
    year = '2018'
    question = '10b_final'
    file = open('../../questions/' + year + '/' + question + '.txt', 'r')
    # file = open('../../questions/example/ADFGVX.txt')
    text = file.read()
    file.close()
    # text = reverse_text(text)
    # show_frequency(text, True)
    show_frequency(text, False, title=question)
    # show_ioc(text, 50, True)
    # show_ioc(text, 50, False)
    # show_n_gram_frequency(text, 2, top=20)
    # show_n_gram_frequency(text, 3, top=10)
    show_frequency(False, True)
    # show_n_gram_frequency(False, 2, top=20)
    # show_n_gram_frequency(False, 3, top=10)
    # check_two_same_letters(text)
