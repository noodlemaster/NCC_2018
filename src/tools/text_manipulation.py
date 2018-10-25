import math

def removespace(text):
    textnospace = []
    for c in text:
        if c.isalpha():
            textnospace.append(c.lower())
    return textnospace

def textksplit(text, n):
    listofchars = []
    for r in range(n):
        chars = []
        for i in range(math.ceil(len(text)/n)):
            try:
                chars.append(text[i*n+r])
            except IndexError:
                break
        listofchars.append(chars)
    return listofchars

def reverse_text(text):
    l = len(text)
    newstring = ""
    for i in range(l):
        newstring += text[l-i]
    return newstring

if __name__ == '__main__':
    text = "XSFJD JMNRF RUDJV LMYFT GWWHP TUDIA HWRMS XXAHJ DNBRH QTOFF NWFGH GLDJJ ATQWH UEQEM DMHRH LMCGL ZAYBT HUWIC "
    text = "apple was great"
    # print(textksplit(removespace(text), 4))
    print(reverse_text(text))