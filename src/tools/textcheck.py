def isuppers(text):
    for t in text:
        if t.isupper():
            return True
    return False

if __name__ == '__main__':
    file = open('./questions/2017/4a_a.txt', 'r')
    text = file.read()
    file.close()
    print(isuppers(text))