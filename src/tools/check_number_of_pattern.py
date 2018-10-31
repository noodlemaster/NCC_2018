alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
def get_key(item):
    return item[0]

if __name__ == '__main__':
    year = '2016'
    question = '8b'
    file = open('../../questions/' + year + '/' + question + '.txt', 'r')
    original = file.read()
    original = original.replace(' ', '')
    original = original.replace('2', ',')
    lines = original.split(',')
    file.close()
    all_list = []
    for line in lines:
        text = line.strip()
        all_list.append(text)
    numlists = []
    for i in range(int(len(all_list)/5)):
        for j in range(len(all_list[i*5])):
            numlist = []
            for k in range(5):
                numlist.append(all_list[i*5+k][j])
            numlists.append(numlist)
    print(numlists)
    num_list = []
    for num in numlists:
        strnum = ''.join(num)
        number = int(strnum, 2)
        num_list.append(number)

    print(num_list)

    all_list = []
    for num in numlists:
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

    text_list = []
    for l in num_list:
        for j in range(len(all_list)):
            if l == all_list[j][0]:
                text_list.append(alphabets[j])
    print(text_list)
    text = ''.join(text_list)
    print(text)