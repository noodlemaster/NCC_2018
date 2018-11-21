import re
import random
import threading
import os
import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib.animation import FuncAnimation
from src.tools.checkenglishness import get_english_score
from src.tools.text_manipulation import text_split_in_order

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']

'''NO I'''
def form_grid(keyword):
    table = []
    list_keyword = []
    for i in range(len(keyword)):
        if keyword[i].upper() not in list_keyword:
            list_keyword.append(keyword[i].upper())
    for each in alphabets:
        if each not in list_keyword:
            list_keyword.append(each)
    if list_keyword.index('I') > list_keyword.index('J'):
        list_keyword[list_keyword.index('I')] = 'J'
        list_keyword.remove(list_keyword[list_keyword.index('J')])
    else:
        list_keyword.remove(list_keyword[list_keyword.index('I')])
    # if list_keyword.index('J') > list_keyword.index('I'):
    #     list_keyword.remove(list_keyword[list_keyword.index('J')])
    # else:
    #     list_keyword.remove(list_keyword[list_keyword.index('I')])
    #     list_keyword[list_keyword.index('J')] = 'I'

    while len(list_keyword)>0:
        row = list_keyword[0:5]
        table.append(row)
        del list_keyword[:5]

    #print(table)
    return table

def get_coordinate(table, target):
    for y in range(0, len(table)):
        for x in range(0, len(table[y])):
            if table[y][x] == target:
                return (x, y)

def horizontal_shift(coordinate, direction_right = 1):
    new_x = (coordinate[0]+direction_right)%5
    return (new_x, coordinate[1])

def verticle_shift(coordinate, direction_down = 1):
    new_y = (coordinate[1]+direction_down)%5
    return (coordinate[0], new_y)

def rectangle_shift(coordinate_a, coordinate_b):
    delta_x = abs(coordinate_a[0] - coordinate_b[0])
    if coordinate_a[0] > coordinate_b[0]:
        coord_b = (coordinate_b[0] + delta_x, coordinate_b[1])
        coord_a = (coordinate_a[0] - delta_x, coordinate_a[1])
    else:
        coord_a = (coordinate_a[0] + delta_x, coordinate_a[1])
        coord_b = (coordinate_b[0] - delta_x, coordinate_b[1])
    return coord_a, coord_b

def playfair(text, table, direction_right = 1, direction_down = 1):
    plaintext = []
    text = re.sub('I','J', text)
    #text = re.sub('J', 'I', text)
    bigram_list = text_split_in_order(text, 2)
    for each in bigram_list:
        a = each[0]
        b = each[1]
        coord_a = get_coordinate(table, a)
        coord_b = get_coordinate(table, b)
        if coord_a[1] == coord_b[1]:  #On the same horizontal line
            coord_a = horizontal_shift(coord_a, direction_right)
            coord_b = horizontal_shift(coord_b, direction_right)
        if coord_a[0] == coord_b[0]:  #On the same verticle line
            coord_a = verticle_shift(coord_a, direction_down)
            coord_b = verticle_shift(coord_b, direction_down)
        if coord_a[0] != coord_b[0] and coord_a[1] != coord_b[1]:  #rectangle
            coord_a, coord_b = rectangle_shift(coord_a, coord_b)[0], rectangle_shift(coord_a, coord_b)[1]

        text_a, text_b = table[coord_a[1]][coord_a[0]], table[coord_b[1]][coord_b[0]]
        plaintext.append(text_a)
        plaintext.append(text_b)

    output = ''.join(plaintext)
    return output
    # output = ['NO I and some X needs to be removed: ', ''.join(plaintext)]
    # print(output)

def generate_random_keyword(lowerlimit, upperlimit):
    keyword = ''
    keyword_length = random.randint(lowerlimit, upperlimit)
    #print(keyword_length)
    while keyword_length > 0:
        char = random.choice(alphabets)
        keyword += char
        keyword_length -= 1
    return keyword

def random_swapping(key):
    l = list(key)
    i, j = random.randint(0, len(l)-1), random.randint(0, len(l)-1)
    if i != j:
        pass
    else:
        i = (i + 1)%(len(key))
    l[i], l[j] = l[j], l[i]
    new_key = ''.join(l)
    return new_key

def reverse(key):
    key = key[::-1]
    return key

def random_substitution(key):
    l = list(key)
    i = random.randint(0, len(key)-1)
    target = random.choice(alphabets)
    if l[i] != target:
        l[i] = target
    else:
        i  = (i + 1)%(len(key))
        l[i] = target
    new_key = ''.join(l)
    return new_key

def random_change_keyword_length(key):
    def add():
        i = random.randint(1, 5)
        part = generate_random_keyword(1, i)
        return part
    def minus():
        i = random.randint(1, len(key)-1)
        return i

    meth = ['add', 'minus']
    if len(key) < 3:
        return add() + key
    else:
        method = random.choice(meth)
        if method == 'add':
            return add() + key
        else:
            j = minus()
            return key[:j]

def random_minor_change():
    methods = [random_swapping, reverse, random_substitution]
    meth = random.choices(methods, [0.25, 0.25, 0.7], k=1)
    return meth[0]

def check_negative_element(list):
    for each in list:
        if each < 0:
            return True
        else:
            return False

def display_data(x, y):
    # fig = plt.figure()
    # ax1 = fig.add_subplot(111)
    # fig.suptitle('Hill Climbing')
    # plt.xlabel('Count')
    # plt.ylabel('Englishness score')
    # plt.axis([0, 10**3, 0, 500])
    # ax1.scatter(x, y)
    # plt.pause(0.02)
    # plt.draw()
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    fig.suptitle('Hill Climbing')
    plt.xlabel('Count')
    plt.ylabel('Englishness score')
    plt.axis([0, 10**3, 0, 500])
    point = ax1.scatter(x, y)
    def animation():
        point.set_xdata(x)
        point.set_ydata(y)
        #return point
    # def update():
    #     return x, y
    anim = FuncAnimation(fig, animation, frames=10, interval=200, blit=True)
    plt.show()
    return anim
    #plt.show()



def update(frame):
    dir_path = str(os.getcwd()).replace('\\', '/')
    try:
        plot_data = np.load(dir_path + '/hill_data.npy')
    except:
        plot_data = np.array([])
    plt.cla()
    ln = plt.plot(plot_data, 'ro')
    return ln

def display_live():
    fig, ax = plt.subplots()
    ax.set_ylim(0, 400)
    time.sleep(3)
    ani = FuncAnimation(fig, update, interval=1000)
    plt.show()

def hill_climbing(display = False):
    highest_score = 0
    highest_likely_key = ''
    parent_keyword = generate_random_keyword(6, 6)
    parent_score = get_english_score(playfair(text, form_grid(parent_keyword), direction_right=-1, direction_down=-1))
    #start_score = get_english_score(playfair(text, form_grid(parent_keyword), direction_right=-1, direction_down=-1))
    count = 1
    unsuccessful = 0
    plot_data = np.array([])
    if display:
        thread = threading.Thread(target=display_live)
        thread.start()
    while True:
        unsuccessful_threshold = 2000
        count += 1
        dG_list = []
        meth = random_minor_change()
        child_keyword = meth(parent_keyword)
        output = playfair(text, form_grid(child_keyword), direction_right=-1, direction_down=-1)
        child_score = get_english_score(output)
        dF = child_score - highest_score
        dG = child_score - parent_score
        parent_score = child_score
        parent_keyword = child_keyword
        meth = str(meth).split(' ')[1]

        plot_data = np.append(plot_data, round(child_score, 1))
        np.save('hill_data', plot_data)
        if dF > 0:
            unsuccessful = 0
            highest_likely_key = child_keyword
            highest_score = child_score
            # parent_score = child_score
            # parent_keyword = child_keyword
            print('Iteration ' + str(count) + '   child keyword: ' + child_keyword + '  child score: ' + str(
                child_score) + '   Method: ' + meth + '  Highest score: ' + str(highest_score))

        # elif dG < 0:
        #     unsuccessful += 1
        #
        # elif dG > 0 and dF < 0:
        #     print('Iteration ' + str(count) + '   child keyword: ' + child_keyword + '  child score: ' + str(
        #         child_score) + '   Method: ' + meth + '  Highest score: ' + str(highest_score))
        #     unsuccessful = 0

        else:
            e = 2.71828
            T = (21**(-count-20)) + 1
            probability = (e**(dF/T))*100
            if 100 - probability < 10:
                unsuccessful = 0
                # parent_score = child_score
                # parent_keyword = child_keyword
                print('Iteration ' + str(count) + '   child keyword: ' + child_keyword + '  child score: ' + str(
                    child_score) + '   Method: ' + str(meth) + '  Highest score: ' + str(highest_score) + '       Probability: ' + str(probability))

            else:
                unsuccessful = unsuccessful + 1

        if unsuccessful > unsuccessful_threshold:
            print('Reached maxima')
            print('NO I and some X needs to be removed : ', playfair(text, form_grid(highest_likely_key), direction_right=-1, direction_down=-1))
            break
        else:
            continue

if __name__ == '__main__':
    file = open('../../../questions/example/playfair_1.txt')
    text = file.read()
    file.close()
    #form_grid('noodle')
    #print(get_english_score(playfair(text, form_grid('noodle'), direction_right = -1, direction_down = -1)))
    #print(get_coordinate(form_grid('noodle'), 'D'))
    #print(rectangle_shift((4,3), (3,0)))
    #generate_random_keyword(2, 18)
    hill_climbing(display=True)
    #display_data(1,1)