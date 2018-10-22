from matplotlib import pyplot

from src.tools.frequency import get_frequency
from src.tools.index_of_coincidence import get_average_ioc_from_1_to_k

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

def show_frequency(text, alp = True):
    frequency = get_frequency(text)
    pyplot.title('Character frequency')
    list = []
    for i in range(26):
        list.append(i)
    if alp:
        pyplot.bar(list, frequency, tick_label=alphabet)
    else:
        pyplot.bar(list, frequency, tick_label=list)
    pyplot.hlines(0.12702, 0, 27)
    pyplot.hlines(0.09056, 0, 27)
    pyplot.show()

def show_ioc(text , n):
    iocs = get_average_ioc_from_1_to_k(text, n)
    pyplot.title('IOCs')
    list = []
    for i in range(n):
        list.append(i+1)
    pyplot.bar(list, iocs)
    pyplot.hlines(0.0667, 0, n + 1)
    pyplot.show()

if __name__ == '__main__':
    file = open('../../questions/2017/5a_2.txt', 'r')
    text = file.read()
    file.close()
    show_frequency(text)
    show_ioc(text, 20)