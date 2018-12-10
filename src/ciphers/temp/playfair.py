from src.tools.text_manipulation import text_split_in_order
from src.tools.hill_climbing import *
from src.tools.hill_climbing_DoublePlayfair import *

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']

'''NO J'''
def form_grid(keyword, replaced = 'J', replacment = 'I'):
    if type(keyword) is list:
        return keyword
    else:
        table = []
        list_keyword = []
        for i in range(len(keyword)):
            if keyword[i].upper() not in list_keyword:
                list_keyword.append(keyword[i].upper())
        for each in alphabets:
            if each not in list_keyword:
                list_keyword.append(each)
        if list_keyword.index(replaced) > list_keyword.index(replacment):
            list_keyword.remove(list_keyword[list_keyword.index(replaced)])
        else:
            list_keyword.remove(list_keyword[list_keyword.index(replacment)])
            list_keyword[list_keyword.index(replaced)] = replacment

        while len(list_keyword)>0:
            row = list_keyword[0:5]
            table.append(row)
            del list_keyword[:5]


        return table

def get_coordinate(table, target):
    for y in range(0, len(table)):
        for x in range(0, len(table[y])):
            if table[y][x] == target:
                return (x, y)

def horizontal_shift(coordinate, grid, direction_right = 1):
    new_x = (coordinate[0]+direction_right)%(len(grid[0]))
    return (new_x, coordinate[1])

def verticle_shift(coordinate, grid, direction_down = 1):
    new_y = (coordinate[1]+direction_down)%(len(grid))
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

# def swap_two_coordinates(coord1, coord2):
#     coord1, coord2 = coord2, coord1

def playfair(text, keyword, direction_right = -1, direction_down = -1):
    table = form_grid(keyword)
    #print(table)
    plaintext = []
    #text1 = re.sub('I','J', text) #no I
    text1 = re.sub('J', 'I', text) #no J
    bigram_list = text_split_in_order(text1, 2)
    for each in bigram_list:
        a = each[0]
        b = each[1]
        coord_a = get_coordinate(table, a)
        coord_b = get_coordinate(table, b)
        #print(a, b, coord_a, coord_b)
        if coord_a[1] == coord_b[1]:  #On the same horizontal line
            coord_a = horizontal_shift(coord_a, table, direction_right)
            coord_b = horizontal_shift(coord_b, table, direction_right)
        if coord_a[0] == coord_b[0]:  #On the same verticle line
            coord_a = verticle_shift(coord_a, table, direction_down)
            coord_b = verticle_shift(coord_b, table, direction_down)
        if coord_a[0] != coord_b[0] and coord_a[1] != coord_b[1]:  #rectangle
            coord_a, coord_b = rectangle_shift(coord_a, coord_b)[0], rectangle_shift(coord_a, coord_b)[1]

        text_a, text_b = table[coord_a[1]][coord_a[0]], table[coord_b[1]][coord_b[0]]
        plaintext.append(text_a)
        plaintext.append(text_b)

    output = ''.join(plaintext)
    return output

def join_2grids(grid1, grid2, TypeOfJoin):
    newgrid = []
    if TypeOfJoin == 'Horizontal' or TypeOfJoin == 'horizontal':
        for i in range(len(grid1)):
            newgrid.append(grid1[i] + grid2[i])
    elif TypeOfJoin == 'Vertical' or TypeOfJoin == 'vertical':
        for i in range(len(grid1)):
            newgrid.append(grid1[i])
        for i in range(len(grid2)):
            newgrid.append(grid2[i])
    else:
        raise ValueError('TypeOfJoin should be either horizontal or vertical')
    return newgrid

def gridTObiggrid(gridbefore, coordinate, TypeOfJoin):
    x, y = coordinate[0], coordinate[1]
    if TypeOfJoin == 'Horizontal' or TypeOfJoin == 'horizontal':
        return (x + len(gridbefore[0]), y)
    elif TypeOfJoin == 'Vertical' or TypeOfJoin == 'vertical':
        return (x, y + len(gridbefore[0]))
    else:
        raise ValueError('TypeOfJoin should be either horizontal or vertical')

def double_playfair(text, keyword1, keyword2, TypeOfJoin = 'Horizontal'):  #typeofjoin = Horizontal or Vertical
    grid1, grid2 = form_grid(keyword1), form_grid(keyword2)
    plaintext = ''
    PlainText = re.sub(r'\W', '', text)
    # text1 = re.sub('I','J', text) # NO I
    text1 = re.sub('J', 'I', PlainText).upper()  # NO J
    bigram_list = text_split_in_order(text1, 2)
    biggrid = join_2grids(grid1, grid2, TypeOfJoin)
    if TypeOfJoin == 'Horizontal' or TypeOfJoin == 'horizontal':
        for each in bigram_list:
            a = each[0]
            b = each[1]
            coord_b = get_coordinate(grid1, b)
            coord_a = gridTObiggrid(grid1, get_coordinate(grid2, a), TypeOfJoin)
            # print(a, b, coord_a, coord_b)
            if coord_a[1] == coord_b[1]:  #On the same horizontal line
                coord_a, coord_b = coord_b, coord_a
            if coord_a[0] != coord_b[0] and coord_a[1] != coord_b[1]:  #rectangle
                coord_a, coord_b = rectangle_shift(coord_a, coord_b)[0], rectangle_shift(coord_a, coord_b)[1]

            text_a, text_b = biggrid[coord_a[1]][coord_a[0]], biggrid[coord_b[1]][coord_b[0]]
            # print(a, b, text_a, text_b)
            plaintext += text_a
            plaintext += text_b
            # output = ''.join(plaintext)
            # return output
    elif TypeOfJoin == 'Vertical' or TypeOfJoin == 'vertical':
        for each in bigram_list:
            a = each[0]
            b = each[1]
            coord_b = get_coordinate(grid1, b)
            coord_a = gridTObiggrid(grid1, get_coordinate(grid2, a), TypeOfJoin)
            #print(a, b, coord_a, coord_b)
            if coord_a[0] == coord_b[0]:  #On the same verticle line
                pass
            if coord_a[0] != coord_b[0] and coord_a[1] != coord_b[1]:  #rectangle
                coord_a, coord_b = rectangle_shift(coord_a, coord_b)[0], rectangle_shift(coord_a, coord_b)[1]

            text_a, text_b = biggrid[coord_a[1]][coord_a[0]], biggrid[coord_b[1]][coord_b[0]]
            # print(a, b, text_a, text_b)
            plaintext += text_a
            plaintext += text_b

    return plaintext

def double_playfair_SA(text, keyword):
    #print(keyword)
    key1, key2 = keyword.split(' ')[0], keyword.split(' ')[1]
    return double_playfair(text, key1, key2)

if __name__ == '__main__':
    file = open('../../../questions/example/doubleplayfair_horizontal.txt')
    text = file.read()
    file.close()

    config = {
        'T0': 33,
        'T_lowest': 0,
        'NumberOfIterationPerT': 1000,
        'FunctionT': T_minus,
        'CipherType': playfair,
        'Keyword/Grid': 'keyword',  #grid/keyword
        'LengthOfKey_lower': 5,
        'LengthOfKey_upper': 16,
        'Probability_threshold': 0.8
    }

    config_double = {
        'T0': 40,
        'T_lowest': 0,
        'NumberOfIterationPerT': 1000,
        'FunctionT': T_mutilier,
        'CipherType': double_playfair_SA,
        'Keyword/Grid': 'keyword',  # grid/keyword
        'LengthOfKey_lower': 10,
        'LengthOfKey_upper': 19,
        'Probability_threshold': 0.8
    }
    # hill_climbing(text, config)
    # print(get_english_score(playfair(text, 'KUPTVNXHLSCWBGDROFAJQEMYZ')))
    #form_grid('FAOJBY')
    # print(playfair(text, 'NIODLE'))
    #print(get_coordinate(generate_random_5x5grid(), 'R'))
    #form_grid('JHGCAY')
    #print(len(generate_random_5x5grid('J')))
    # print(double_playfair_SA(text, 'KEY WORD'))
    hill_climbing_DoublePlayfair(text, config_double)
    # print(double_playfair(text, 'KEY', 'WORD'))