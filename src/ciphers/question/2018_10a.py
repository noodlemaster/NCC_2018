from src.tools.text_manipulation import text_split_in_order

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

def get_key(item):
    return item[0]


year = '2018'
question = '10a'
file = open('../../../questions/' + year + '/' + question + '.txt', 'r')
original = file.read()
texts = text_split_in_order(original, 5)

all_list = []
for num in texts:
    found = False
    strnum = ''.join(num)
    number = int(strnum, 2)
    for each in all_list:
        if each[0] == number:
            each[1] += 1
            found = True
            break
    if not found:
        all_list.append([number, 1])
all_list = sorted(all_list, key=get_key)
print(all_list)
print(len(all_list))

for num in texts:
    found = False
    strnum = ''.join(num)
    number = int(strnum, 2)
    print(alphabets[number], end='')

