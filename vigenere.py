import math

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

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

def count_alphabet(text, alphabet):
    alphabet_count = [0] * len(alphabet)
    for i in range(len(alphabet)):
        for c in text:
            if c == alphabet[i].lower():
                alphabet_count[i] += 1
    return alphabet_count

def calculate_ioc(alphabet_count):
    total = 0
    for i in alphabet_count:
        total += i
    prob = 0.0
    for n in alphabet_count:
        prob += (n*(n-1))
    prob /= (total*(total-1))
    return prob

if __name__ == '__main__':
    #vigenere
    text = "XSFJD JMNRF RUDJV LMYFT GWWHP TUDIA HWRMS XXAHJ DNBRH ,QTOFF NWFGH GLDJJ ATQWH UEQEM DMHRH LMCGL ZAYBT HUWIC ,MHDJI CGFVZ TJHWR FYBXB HTTLX AHFLY MHDKM ZKTPS SUMRH ,FHLRU WATHU JVLTQ LZSGS NAFWL WUGXD UYCHS WZJWH SIAIY ,GYLSQ CMDDF IMXHX JNNRY REFEX NWHTM LNEDJ CYDRM HIGXL ,VJLXQ HUYLH SLUYL TSVSH NBTQK FHWTQ DNHXU DQRYG YVSQF ,MMRKJ QHZOV SIMGH HTMLN EDJQB YKGZN XSFJD JMNRF XUBIG ,JRUKP PSSOE NVSXY GNRJQ YVYXJ JLBSF JDJMT JJFJA DDLYB ,XZQAA YKXLL DIYXX JWYRF WAYML NPHQY LYHFH LRUWA THBXD ,DQUUT XLYLT SVXTL FNQYN HMJOD NABGO WSOFG HJXIK YHPYM ,HZQVX UGILE FAXXL FYITX WJJUF TIFTH LJQKJ NAJUW FLXRD ,FDGTS BOFSL YRHJL YTUEY BTYWJ FHLKR JRUMN RFXIF JVLWU ,BLKLK IKBDJ IUGIV GRYOJ UQHIF UOWCG HXWAS PHQYW XQTUS ,ASAEJ WLJLL KRJSO FGHJX UGIXK JGTYK KYIWT WZJNK FQKKI ,KRDLN IGMRO JPXWQ GRUMY HJBBB HKEJN ATGAX OLJGL MYKJV ,MQNBS JKHLT REDJX WFWSX NKJDE XBHZO VLCOJ QGMCG YVSGI ,NYKGB CMBDK JHVWB HYYWI XJNHZ BRJQX PFUAN NAJDD QCXXV ,UTLXI VGRYG TWSGF XALUY IKNHK FATNQ KYNAJ JWWGT SVTJW ,TZVWY BXNUW SWKDS LNIGX BKYYF XGAIH HYVMK ZBHLW SNEDV ,UWUFG OWRYL XDYJM KNJGW INXPS YBXRD LNWTQ DFFFR XLKGS ,TQOAJ XVTGW HLTHN WWMEF LVGUK JSSYN XWQKM CWIHF BCMML ,FYBXR HKXUZ JVSSX NXHVY BXRWG WYVWH SYYMM HEFWA NQWZM ,XIWGJ HVWBH YNAJP LMILJ FGIYL WHNTF OJGSW INSGL MYNXH ,GKMXH UWYEX DVLMU MBHJJ MAFUW IUFTQ YYBHX HOMIG JHVJX ,MTFGR GNSLU FNXXH UZLXQ BLMYL JDJJE GTZFF MLDPE JNKNF ,WSWKD SLNIG XBKYY FXDFI BTAHS BYTPQ WXMBS WZFNX AHJDI ,GJLFA IEAHV MULYR HTMLJ VKYBX XDEJM XYRXX YVWHL PYRX "
    #transposition
    text = "SIEID ATTPW ADIVL SOLWO IYMRD AOSTT TDUHM AGTTT HSEOO  TAEST EOGNU AEDLN HNRDH KIWOA MENEE INEAS NPAIT SLIAI  AOJDN TCAET SOKEE EIULD HRAUE WSYSA IRBCT WNNSN TARHH  SUHAS MNOAG SVEPI AGINE IOAIS EBGRS TTWYO GTLNO EVMRT  WGTOI SAHHI ECAWP HTRAO TCRTS YRBYG  "
    for k in range(1, 9 + 1):
        texts = textksplit(removespace(text), k)
        # for text in texts:
        #     num = count_alphabet(text, alphabet)
        #     prob = calculate_ioc(num)
        #     print(prob)
        num = count_alphabet(texts[0], alphabet)
        prob = calculate_ioc(num)
        print(prob)