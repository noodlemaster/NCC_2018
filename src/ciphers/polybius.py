import itertools
from src.ciphers.hill import *
from src.tools.checkenglishness import *

standard_noJ = [[], ['', 'A', 'B', 'C', 'D', 'E'], ['', 'F', 'G', 'H', 'I', 'K'], ['', 'L', 'M', 'N', 'O', 'P'], ['','Q', 'R', 'S', 'T', 'U'], ['','V', 'W', 'X', 'Y', 'Z']]
standard_noZ = [[], ['', 'A', 'B', 'C', 'D', 'E'], ['', 'F', 'G', 'H', 'I', 'J'], ['', 'K', 'L', 'M', 'N', 'O'], ['','P', 'Q', 'R', 'S', 'T'], ['','U', 'V', 'W', 'X', 'Y']]
standard_noV = [[], ['', 'A', 'B', 'C', 'D', 'E'], ['', 'F', 'G', 'H', 'I', 'J'], ['', 'K', 'L', 'M', 'N', 'O'], ['','P', 'Q', 'R', 'S', 'T'], ['','U', 'W', 'X', 'Y', 'Z']]
standard_noK = [[], ['', 'A', 'B', 'C', 'D', 'E'], ['', 'F', 'G', 'H', 'I', 'J'], ['', 'L', 'M', 'N', 'O', 'P'], ['','Q', 'R', 'S', 'T', 'U'], ['','V', 'W', 'X', 'Y', 'Z']]
standard_noC = [[], ['', 'A', 'B', 'D', 'E', 'F'], ['', 'G', 'H', 'I', 'J', 'K'], ['', 'L', 'M', 'N', 'O', 'P'], ['','Q', 'R', 'S', 'T', 'U'], ['','V', 'W', 'X', 'Y', 'Z']]
standard_noW = [[], ['', 'A', 'B', 'C', 'D', 'E'], ['', 'F', 'G', 'H', 'I', 'J'], ['', 'K', 'L', 'M', 'N', 'O'], ['','P', 'Q', 'R', 'S', 'T'], ['','U', 'V', 'X', 'Y', 'Z']]
standard_extended = [[], ['', 'A', 'B', 'C', 'D', 'E', 'F'], ['', 'G', 'H', 'I', 'J', 'K', 'L'], ['', 'M', 'N', 'O', 'P', 'Q', 'R'], ['', 'S', 'T', 'U', 'V', 'W', 'X'], ['', 'Y', 'Z', '0', '1', '2', '3'], ['4', '5', '6', '7', '8', '9']]

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def group(text):
    PlainText = re.sub(r'\W', '', text)
    list1 = group_text(PlainText, 2)
    return list1

def get_existing_characters(text):
    PlainText = re.sub(r'\W', '', text)
    l = []
    for i in range(0, len(PlainText)):
        l.append(PlainText[i])
    l = list(set(l))
    return l

    # position = []
    # for each in l:
    #     pos = alphabet.index(each)
    #     position.append(pos)
    # order = []
    # num = []
    # mapping = []
    # position = sorted(position, key=int)
    # for each in position:
    #     order.append(alphabet[each])
    # for i in range(1, len(position)+1):
    #     num.append(i)
    # for char in l:
    #     for number in num:
    #         mapping.append([char, str(number)])
    # print(mapping)
def permutation(iterable):
    result = list(map("".join, itertools.permutations(iterable)))
    return result

def get_mapping(template):
    mapping = []
    big_table = []
    perm = permutation(get_existing_characters(text))
    for each in perm:
        perm2 = each
        table = [[]]
        row1 = ['', each[0]+perm2[0], each[0]+perm2[1], each[0]+perm2[2], each[0]+perm2[3], each[0]+perm2[4]]
        row2 = ['', each[1]+perm2[0], each[1]+perm2[1], each[1]+perm2[2], each[1]+perm2[3], each[1]+perm2[4]]
        row3 = ['', each[2]+perm2[0], each[2]+perm2[1], each[2]+perm2[2], each[2]+perm2[3], each[2]+perm2[4]]
        row4 = ['', each[3]+perm2[0], each[3]+perm2[1], each[3]+perm2[2], each[3]+perm2[3], each[3]+perm2[4]]
        row5 = ['', each[4]+perm2[0], each[4]+perm2[1], each[4]+perm2[2], each[4]+perm2[3], each[4]+perm2[4]]
        table.append(row1)
        table.append(row2)
        table.append(row3)
        table.append(row4)
        table.append(row5)
        big_table.append(table)
    for each in big_table:
        #print(each)
        for i in range(1, 6):
            for j in range(1, 6):
                mapping.append([each[i][j], template[i][j]])
    return mapping

def group_list(list, n):
    new_list = []
    for i in range(0, len(list), n):
        subList = list[i:i+n]
        new_list.append(subList)
    return new_list

def substitution_char(text, mapping):
    grouped = group(text)
    PlainText = re.sub(r'\W', '', text)
    for i in range(0, len(grouped)):
        for map in mapping:
            if grouped[i] == map[0]:
                grouped[i] = map[1]
    new_text = ''.join(grouped)
    return new_text

def substitution(text, mapping):
    PlainText = re.sub(r'\W', '', text)
    for each in mapping:
        old, new = each[0], str(each[1]).lower()
        PlainText = re.sub(old, new, PlainText)
    print(PlainText)
    return PlainText

def polybius_char(text):
    result = []
    template_list = [standard_noJ, standard_noK, standard_noC, standard_noV, standard_noW, standard_noZ]
    warning = ['No J: ', 'No K: ', 'No C: ', 'No V: ', 'No W: ', 'No Z: ', ]
    for i in range(0, len(template_list)):
        template = template_list[i]
        mapping = group_list(get_mapping(template), 25)
        for each in mapping:
            result.append([warning[i], substitution_char(text, each)])

    top_score = []
    for each in result:
        target = each[1]
        score = get_english_score(target)
        top_score.append(score)

    howmany = 5

    for i in range(1, howmany+1):
        highscore = sorted(top_score)[-i]
        index = top_score.index(highscore)
        if isinstance(index, int):
            print(top_score[index], result[index])

def polybius_num(text):
    l_noJ_yx, l_noJ_xy = [], []
    l_noZ_yx, l_noZ_xy = [], []
    l_noV_yx, l_noV_xy = [], []
    l_noW_yx, l_noW_xy = [], []
    l_noK_yx, l_noK_xy = [], []
    l_noC_yx, l_noC_xy = [], []
    l_extend_yx, l_extend_xy = [], []
    list_grouped = group_text(text, 2)
    for each in list_grouped:
        x, y = int(each[0]), int(each[1])
        l_noJ_yx.append(standard_noJ[x][y])
        l_noZ_yx.append(standard_noZ[x][y])
        l_noV_yx.append(standard_noV[x][y])
        l_noW_yx.append(standard_noW[x][y])
        l_noK_yx.append(standard_noK[x][y])
        l_noC_yx.append(standard_noC[x][y])
        l_extend_yx.append(standard_extended[x][y])
        l_noJ_xy.append(standard_noJ[y][x])
        l_noZ_xy.append(standard_noZ[y][x])
        l_noV_xy.append(standard_noV[y][x])
        l_noW_xy.append(standard_noW[y][x])
        l_noK_xy.append(standard_noK[y][x])
        l_noC_xy.append(standard_noC[y][x])
        l_extend_xy.append(standard_extended[y][x])
    print('No J: '+''.join(l_noJ_yx))
    print('No J: '+''.join(l_noJ_xy))
    print('No Z: '+''.join(l_noZ_yx))
    print('No Z: '+''.join(l_noZ_xy))
    print('No V: '+''.join(l_noV_yx))
    print('No V: '+''.join(l_noV_xy))
    print('No W: '+''.join(l_noW_yx))
    print('No W: '+''.join(l_noW_xy))
    print('No K: '+''.join(l_noK_xy))
    print('No K: '+''.join(l_noK_yx))
    print('No C: '+''.join(l_noC_xy))
    print('No C: '+''.join(l_noC_yx))
    print('normal: '+''.join(l_extend_yx))
    print('normal: '+''.join(l_extend_xy))

def polybius(text):
    PlainText = re.sub(r'\W', '', text)
    if re.search(r'\D', PlainText):
        polybius_char(text)
    else:
         polybius_num(text)

if __name__ == '__main__':
    #----IMPORTANT----
    #--Check spelling!!!!!!! check where to put the missing letter which is shown at front!!--
    file = open('../../questions/2017/3b.txt', 'r')
    text = file.read()
    file.close()
    #text = '442315354224321532243324434415425224313144425444341334335124331315154531151114154243443412111325231542113535423411132352231533432315111414421543431543442315321215213442151424333315423111441542124544155335151344114424343343342111124215112544234234452223114215313452522444234411312543141511143134132515143451154244231524422443231234421415422443434515'
    polybius(text)