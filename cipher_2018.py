import math
import re

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

def extract_text():
    text = "UCGGP,V CZ LOGP TGCJOSKY SDG JUO SVYO DB WDRVO. SDYYDMVBT PDKG JVEDSS CADKJ UOG JGCLOY MO JGCIXOR UOG JD C ADDX JGCROG VB OY-XUCYVYV HDKX,  EKJ C JCVY DB UOG CBR V UCLO AOOB ICGGPVBT DKJ C SOM ACIXTGDKBR IUOIXH DS ZP DMB. YVXO PDK V SDKBR YVJJYO JD GCVHO ZP HKHEVIVDBH, CBR, TVLOB UOG EGDSOHHVDB, JUOGO VH BDJUVBT KBKHKCY CADKJ UOG AOVBT UOGO VB ICVGD. HUO HOOZH JD AO MOYY XBDMB, MOYY YVXOR, CBR ZDHJ VZEDGJCBJYP, MOYY JGKHJOR. VS MO UCR BDJUVBT OYHO JD TD DB V JDD MDKYR UCLO MGVJJOB UOG DSS CH C YOCR, UDMOLOG JMD RCPH CTD ZP CTOBJH YDHJ JGCIX DS UOG CBR HUO RVHCEEOCGOR.MO GCB CYY JUO KHKCY IUOIXH CBR SDKBR UOG VB IYODECJGC UDHEVJCY, GOIDLOGVBT SGDZ CB CHHCKYJ. JUO YDICY HJCJVDB EGDIKGOR IGOROBJVCYH CBR IDLOG SDG ZO CH C YDICY ROJOIJVLO CBR V ICGGVOR DKJ C HJCBRCGR SVOYR VBJOGLVOM MUVIU UCH TVLOB KH C UOCRHJCGJ DB JUO VBLOHJVTCJVDB. WDRVO'H ZVHSDGJKBO VH ZP YKIX.HUO VH UOGO JD JGCIX RDMB C RDIKZOBJ CEECGOBJYP MGVJJOB AP JUO GDZCB UVHJDGVCB JCIVJKH. JUO UKBJ SDG JUO ADDX HJCGJOR MUOB HDZODBO SDKBR C RDIKZOBJ VB JUO LCJVICB YVAGCGP MGVJJOB AP YC JDKGOJ. VJ VBIYKROR ONJGCIJH SGDZ C YCJVB RDIKZOBJ JUCJ CEEOCGOR JD AO CB ORVJOR LOGHVDB DS JUO CTGVIDYC CBR WDRVO JOYYH ZO JUCJ JUO HJPYO MCH GOIDTBVHCAYP JCIVJKH, CBR HDZO DS JUO HOBJOBIOH MOGO JUO HCZO CH XBDMB LOGHVDBH DS JUO DGVTVBCY. UDMOLOG JUOGO MOGO C SOM HVTBVSVICBJ IUCBTOH CBR WDRVO JGCLOYYOR JD GDZO JD HOCGIU SDG ZDGO. VB JUO CGIUVLOH HUO SDKBR JCIVJKH’ ROCJUAOR IDBSOHHVDB MUVIU GOSOGGOR JD C RDIKZOBJ HD HUDIXVBT JUCJ JCIVJKH UVZHOYS UCR DGROGOR VJ JD AO HEYVJ KE CBR IDBIOCYOR CIGDHH C BKZAOG DS HVJOH VB JUO CBIVOBJ MDGYR. BD IYKOH MOGO TVLOB JD JUO BCJKGO DS JUO HVJOH, AKJ JUO RDIKZOBJ IDBIYKROR MVJU JUO HJCJOZOBJ “ZP YOTCIP MVYY AO C JGKJU MUVIU DKJYCHJH JUO ZDKBJCVB DS TDRH MUVIU TKCGRH VJH TCJOMCP. JUVH YOR WDRVO JD HKHEOIJ JUCJ JUO EPGCZVRH CJ TVQC MOGO C TDDR EYCIO JD HJCGJ. JUCJ MCH MUOGO HUO MCH CJJCIXOR.VJ JDDX WDRVO JUGOO RCPH JD SVBR JUO RDIKZOBJ UVRROB CZDBT JUO HJDBOH, CBR ZP TKOHH VH JUCJ HDZODBO MCH MCJIUVBT UOG KBJVY HUO SDKBR VJ YCJO DB JUO JUVGR RCP. HUO DBYP UCR VJ SDG SVLO ZVBKJOH AOSDGO HUO MCH GDAAOR, AKJ HUO ZCRO JUO ZDHJ DS JUCJ JVZO, EUDJDTGCEUVBT JUO SGCTZOBJ. JUO CJJCIXOGH JDDX UOG EUDBO, AKJ JUO VZCTO UCR CYGOCRP KEYDCROR JD JUO IYDKR, HD CJ YOCHJ MO XBDM MUCJ VJ HCVR. EOGUCEH ZDGO VZEDGJCBJYP MO ZCP UCLO CBDJUOG IYKO JD JUO YDICJVDB DS JUO BONJ SGCTZOBJ, JUO SKYY JGKJU ZKHJ GOZCVB UVRROB SDG BDM, CBR CH GOZCGXOR AP ZP JGKHJOR HYCLO CBR IDBSVRCBJ JVGD, MUCJ AOJJOG EYCIO JD UVRO C ADDX JUCB CZDBT ADDXH?"
    return text

def frequency(text):
    freq_character = []
    # text = extract_text()
    for j in alphabet:
        result = re.findall(j, text)
        freq_character.append(len(result))
    probability = []
    PlainText = re.sub(r'\W', '', text)
    total_cahracter = len(PlainText)
    for each in freq_character:
        probability.append(int(each) / total_cahracter)
    # print(probability)
    return probability

def guessing(text):
    text = re.sub(r'[^\w\s]', '', text)
    text = text.split(' ')

# for each in text:
#	if len(each) == 3:


def dictionary():
    pass

def x_plus_a_check(index_e, index_t):
    if index_e > 4:
        a = 26 - (index_e - 4)
    else:
        a = 4 - index_e
    if (index_t + a) % 26 == 19:  # check with t
        return a
    else:
        return False

def x_plus_a(index_e, index_t):
    mapping = []
    a = x_plus_a_check(index_e, index_t)
    for i in range(0, 26):
        alphabet_position = (i + a) % 26
        mapping.append([alphabet[i], alphabet[alphabet_position]])  # [encrypt, decrypt]
    # print(mapping)
    return mapping

def ax_plus_b_check(index_e, index_t):
    # [m, m']
    check = []
    modulus_inverse = [[1, 1], [3, 9], [5, 21], [7, 15], [9, 3], [11, 19], [15, 7], [17, 23], [19, 11], [21, 5],
                       [23, 17], [25, 25]]
    m = abs(index_e - index_t)
    for each in modulus_inverse:
        if each[0] == m:
            m_inverse = each[1]
            check.append(1)
        else:
            pass
    if len(check) == 1:
        if index_e > index_t:
            a = ((-15) * m_inverse) % 26
        else:
            a = (15 * m_inverse) % 26
        b = (4 - index_e * a) % 26
        return a, b
    else:
        return False

def ax_plus_b(index_e, index_t):
    mapping = []
    a, b = ax_plus_b_check(index_e, index_t)[0], ax_plus_b_check(index_e, index_t)[1]
    for i in range(0, 26):
        alphabet_position = (a * i + b) % 26
        mapping.append([alphabet[i], alphabet[alphabet_position]])  # [encrypt, decrypt]
    # print(mapping)
    return mapping

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

def Vigenere_check(text):
    text_list = []
    check_list = []
    PlainText = re.sub(r'\W', '', text)
    for i in range(2, 25):
    	listofchar = textksplit(PlainText, i)


def transposition():
    pass

def decrypt():
    text = extract_text()
    probability = frequency(text)
    letter_freq = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094,
                   0.00153, 0.0772, 0.04025, 0.02406, 0.06749, 0.07507, 0.01925, 0.0095,
                   0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.0236, 0.0015, 0.01974, 0.00074]
    maximum_e = max(probability)
    index_e = probability.index(maximum_e)
    maximum_t = sorted(probability)[-2]
    index_t = probability.index(maximum_t)
    if alphabet[index_e] != 'E':
        if maximum_e >= 0.108 and maximum_t >= 0.087:
            if x_plus_a_check(index_e, index_t):
                mapping = x_plus_a(index_e, index_t)
                print('x+a')
            elif ax_plus_b_check(index_e, index_t):
                mapping = ax_plus_b(index_e, index_t)
                print('ax+b')
            else:  # maybe guessing or dictionary
                print('iii')
        elif maximum_e >= 0.112 and maximum_t <= 0.087:
            text = re.sub(alphabet[index_e], 'E', text)
        elif maximum_e < 0.103:
            # Vigenere_check()
            pass
        else:
            pass
    else:
        transposition()

    for each in mapping:
        old, new = each[0], str.lower(each[1])
        text = re.sub(old, new, text)

    print(text)

if __name__ == '__main__':
    decrypt()
    # x_plus_a_check(15, 4)
    # x_plus_a(15, 4)
    #Vigenere_check(extract_text())
