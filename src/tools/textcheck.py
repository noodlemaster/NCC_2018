def isuppers(text):
    for t in text:
        if t.isupper():
            print(t)
            return True
    return False

if __name__ == '__main__':
    file = open('../../questions/2018/10b/10b_working_space.txt', 'r')
    text = file.read()
    # for i in range(7):
    #     file = open('../../questions/2018/10b/10b_k_' + str(i) + '_a.txt', 'r')
    #     text = file.read()
    #     file.close()
    print(isuppers(text))