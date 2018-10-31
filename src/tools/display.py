from matplotlib import pyplot

from src.tools.frequency import get_frequency
from src.tools.index_of_coincidence import get_average_ioc_from_1_to_k, get_first_ioc_from_1_to_k

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

def show_frequency(text, alp = True):
    if text:
        frequency = get_frequency(text)
    else:
        file = open('../../data/letter_frequency.txt', 'r')
        frequency = file.readlines()
        file.close()
        for i in range(len(frequency)):
            frequency[i] = float(frequency[i].strip())/100
    pyplot.title('Character frequency')
    list = []
    list_s = []
    for i in range(26):
        list.append(i)
    if alp:
        pyplot.bar(list, frequency, tick_label=alphabet)
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

if __name__ == '__main__':
    year = '2016'
    question = '8b_3'
    # file = open('../../questions/example/hill2x2.txt', 'r')
    file = open('../../questions/' + year + '/' + question + '.txt', 'r')
    text = file.read()
    file.close()
    show_frequency(False, True)
    show_frequency(text, True)
    show_ioc(text, 55, True)
    show_frequency(text, False)
