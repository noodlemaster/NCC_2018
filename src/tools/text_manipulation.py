import math

def removespace(text):
    textnospace = []
    for c in text:
        if c.isalpha():
            textnospace.append(c)
    return textnospace

def groupcharactors(text, n):
    table = []
    if len(text)%n != 0:
        return table
    row_n = int(len(text)/n)
    for r in range(row_n):
        row = []
        for c in range(n):
            row.append(text[c*row_n + r])
        table.append(row)
    return table

def text_k_split(text, n):
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

def text_split_in_order(text, n):
    listofchars = []
    k = math.ceil(len(text)/n)
    for i in range(k):
        chars = []
        for j in range(n):
            try:
                chars.append(text[n*i + j])
            except IndexError:
                break
        listofchars.append(chars)
    return listofchars

def reverse_text(text):
    l = len(text)
    newstring = ""
    for i in range(l):
        newstring += text[l-1-i]
    return newstring

def output_csv(split_text, name):
    outputfile = open(name + '.csv', 'w')
    for cs in split_text:
        for c in cs:
            outputfile.write(c)
            outputfile.write(',')
        outputfile.write('\n')
    outputfile.close()


if __name__ == '__main__':
    # text = "atadehterucesotdnasisylanarofscisnerofotdessapneebsahhcihwpotpalsronyartnoselifdetpyrcneehtnideniatnocebyamnoitamrofnitahtfollaroemostahteveilebewramladdnaronyartnitseretnignortsaevahyehtyhwdnatsrednuyllufewodronelledaticdnaximanydetacidnyssdpehtneewtebnoitcaretniehtfoerutcipraelcaevahtonodllitsewdnahtaedrehekafotdevirtnocramladwohdnatsrednutonodewnignisolcsitenehttahterawaebotylekilylhgihwonhtoberayehttahtdnaolsoraenronignivilhtoberayehttahteveilebewseiraidisbusstifoenoroelledaticybdetcetorpgniebhtoberadnarehtonaenohtiwnoitacinummocnierayehteveilebewramladailemajsiegatoofehtninamowehttahtdnaronyartnitramsitcepsusehttahtytniatrecraenhtiweveilebewsnoisulcnocecnallievrusnevesruofytnewtrednusiknabolsoehtdnaderotinomgnieberamrifwalehtmorfdnaotsllaclladehctawylesolcgniebsidnaknabehttaygolonhcetretupmocotsseccadesirohtuanuniegagneotycaripsnocfosegrahcgnidnepliabnodesaelersawtcepsusehtelledaticrerutcafunamsmraehtrofskrowhcihwmrifwalaotdegnolebgnarehtahtelibomehtdewohsecartllacallacehtekamotdewollaneebdahehlitnusnoitseuqeromynarewsnaotdesufertcepsusehttubreniaternoreywalaevahotevitcellocgnikcahaforebmemaroflausunusawtitahttuodetniopewreywalsihllacotdednamedyldetaeperdnadetatigaylhgihemacebtcepsusehtsihttuobadeksanehwnoitagitsevnirednudoirepehtgnirudhcnarbemasehttadeoedivnetfosawnoitpircsedsramladgnihctamnamowatahtdecitonoslaewrevewohweivretnitadebircsedehseitivitcaehthtiwdeillaterehtstisivsihtahtdewohssisylanarehtrufdnaknabsihtfoegatoofybboleveirterottneserewstnegahcnarbolsonanimihfoegatoofdahewtahteveilebotdemeesehgnirotinomneebdahewknabssiwsehtmorfknabtnereffidyleritnenatuobagniklatsawtcepsusehttahttnerappaemacebtirevewohgninoitseuqrehtrufrednuevitcellocehtybnekatneebdahnoitcarehtrufonosdnuofneebdahsessenkaewontahtdnaesicrexetahetihwasawtidemialcehsihtfoytilagelehttuobadegnellahcnehwytirucessknabehtfotsetnoitartenepecnaleerfanonoitidepxegnihsihpafotrapsaevitcellocehtfoflahebnodetisivdahehtahtdemialcehdnaknabafoybbolehtnimihfoegatoofdahewtahtdelaeverewredrahgnihsuphtuomotdnahgnivilenoemosrofffollewootebotderaeppaehtahttuodetniopewnehwneveevreserhsacsihtpekeherehwnialpxetondluowrotondluocehsihtnodesserpnehwtubtnuoccaknabaevahottondnasisabhsacanoyleritnekrowotdemialcehtsriftastnemegnarralaicnanifstcepsusehtotdenrutewknabssiwsehthtiwpihsnoitalersronyarttuobanwonkydaerlasawtahwlaeverottoneracgnikattituobaklatotderaperptonsawdnadnihebtahtllatfeldahehtahtdetatstcepsusehtdlihcasaerehtemitfotnuomaelbaredisnocatnepsehtseggusscitsiretcarahceciovtahttcafehtetipsedllatakuehthtiwsknilondnuofsgnignolebstcepsusehtfohcraesanoisserppofolootaerewsesabatadandtahtgnitatssisylanarofelpmasandaedivorpotstseuqerdesuferehnitramebotsemajdetcepsusewtahtlaevertondidewtubronyartnitramfodnatcepsusehtfoscirtemoibehtneewtebnoitalerrocfoeergedhgihadewohssisylanaseitirohtuaytisrevinuehthtiwtuodekcehcyrotssihletahcuenniecneicsretupmocniemmargorpetaudargamorftuopordaebotdemialcdnanitramsemajfoemanehtnistnemucodytitnediytilauqhgihgniyrracsawtcepsusehtsinmorfsperdnaasnimecnadnettanironyartnitramhtiwweivretnimorfseton"
    # print(reverse_text(text))
    # print(textksplit(removespace(text), 4))
    file = open('../../questions/2018/8a.txt', 'r')
    text = file.read()
    file.close()
    # print(reverse_text(text))
    #Trasposition
    # output_csv(text_k_split(removespace(text), 153), '../../questions/2018/6b/2018_6b_14')
    output_csv(text_k_split(removespace(text), int(131*2*8/8)), '../../questions/2018/2018_8a_8')