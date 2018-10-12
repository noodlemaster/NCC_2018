import math

def textksplit(text, n):
    textnospace = []
    for c in text:
        if c != ' ':
            textnospace.append(c)
    listofchars = []
    for r in range(n):
        chars = []
        for i in range(math.ceil(len(textnospace)/n)):
            try:
                chars.append(textnospace[i*n+r])
            except IndexError:
                break
        listofchars.append(chars)
    return listofchars

if __name__ == '__main__':
    text = "XSFJD JMNRF RUDJV LMYFT GWWHP TUDIA HWRMS XXAHJ DNBRH QTOFF NWFGH GLDJJ ATQWH UEQEM DMHRH LMCGL ZAYBT HUWIC "
    text = "apple is great"
    print(textksplit(text, 4))