def extract_alphabets(text):
    textnospace = []
    for c in text:
        if c.isalpha():
            textnospace.append(c)
    return textnospace



def text_replace():
    file = open('../../questions/2018/10b/10b_working.txt', 'r')
    solution = file.read()
    file.close()
    solution = extract_alphabets(solution)

    file = open('../../questions/2018/10b.txt', 'r')
    question = file.read()
    file.close()

    answer = ''

    i = 0
    for c in question:
        if c.isalpha():
            answer = answer + solution[i]
            i = i + 1
        else:
            answer = answer + c

    file = open('../../questions/2018/10b/10b_working_space.txt', 'w')
    file.write(answer)
    file.close()

# print(i)
# print(len(solution))
# print(len(extract_alphabets(question)))
# print(''.join(extract_alphabets(question)))


file = open('../../questions/2018/10b.txt', 'r')
question = file.read()
file.close()

answer = ''

num = [0,1,2,3,4,5,6]
i = 0
for c in question:
    if c.isalpha():
        answer = answer + str(num[i%7])
        i = i + 1
    else:
        answer = answer + c

file = open('../../questions/2018/10b/10b_working_numbers.txt', 'w')
file.write(answer)
file.close()