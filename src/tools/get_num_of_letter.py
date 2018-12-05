from src.ciphers.transposition import extract_alphabets

inputfile = open('../../questions/2018/8a_a.txt', 'r')
text = inputfile.read()
inputfile.close()
text = extract_alphabets(text)
print(text)
print(len(text))
for i in range(len(text)):
    if text[i] == 'h':
        print(i+1, end=",\n")
