turkd=float(raw_input("Türkçe doðru sayýnýzý giriniz:"))
turky=float(raw_input("Türkçe yanlýþ sayýnýzý giriniz:"))
Turkss=turkd+turky
if Turkss<=40:
   TNS=turkd-(turky/4)
   print "TNS",TNS
else:
       print"Geçersiz soru sayýsý girdiniz"
      



matd=float(raw_input("Matematik doðru sayýnýzý giriniz:"))
maty=float(raw_input("Matematik yanlýþ sayýnýzý giriniz:"))
Matss=matd+maty
if Matss<=40:
   MNS=matd-(maty/4)
   print "MNS",MNS
else:
       print"Geçersiz soru sayýsý girdiniz"



sosd=float(raw_input("Sosyal doðru sayýnýzý giriniz:"))
sosy=float(raw_input("Sosyal yanlýþ sayýnýzý giriniz:"))
Sosss=sosd+sosy
if Sosss<=40:
   SNS=sosd-(sosy/4)
   print "SNS",SNS
else:
       print"Geçersiz soru sayýsý girdiniz"



fend=float(raw_input("Fen doðru sayýnýzý giriniz:"))
feny=float(raw_input("Fen yanlýþ sayýnýzý giriniz:"))
Fenss=fend+feny
if Fenss<=40:
   FNS=fend-(feny/4)
   print "FNS",FNS
else:
       print"Geçersiz soru sayýsý girdiniz"

if Turkss<=40 and Matss<=40 and Sosss<=40 and Fenss<=40:
    TP=TNS*4
    MP=MNS*3
    SP=SNS*2
    FP=FNS*1
    YGSPUAN=TP+MP+SP+FP+100
    print "YGSPUAN:",YGSPUAN
else:
    print "Girdiðiniz soru sayýlarýný kontrol ediniz"



EDS=float(raw_input("Edebiyat doðru sayýnýzý giriniz:"))
EYS=float(raw_input("Edebiyat yanlýþ sayýnýzý giriniz:"))
EDEBIYATSS=EDS+EYS
if EDEBIYATSS<=56:
   ENS=EDS-(EYS/4)
   print "ENS",ENS
else:
       print"Geçersiz soru sayýsý girdiniz"


MATD=float(raw_input("Matematik lys doðru sayýnýzý giriniz:"))
MATY=float(raw_input("Matemetik lys yanlýþ sayýnýzý giriniz:"))
MATEMATIKSS=MATD+MATY
if MATEMATIKSS<=80:
   MLNS=MATD-(MATY/4)
   print "MLNS",MLNS
else:
       print"Geçersiz soru sayýsý girdiniz"



COGD=float(raw_input("Coðrafya doðru sayýnýzý giriniz:"))
COGY=float(raw_input("Coðrafya yanlýþ sayýnýzý giriniz:"))
COGSS=COGD+COGY
if COGSS<=24:
   CNS=COGD-(COGY/4)
   print "CNS",CNS
else:
       print"Geçersiz soru sayýsý girdiniz"

if ENS<=56 and MLNS<=80 and CNS<=24:
    ELP=float(ENS*4)
    MLP=float(MLNS*3)
    CLP=float(CNS*1.5)
    LYS=ELP+MLP+CLP
    print "LYS",LYS
else:
    print "Geçersiz soru sayýsý girdiniz"

LO=float(raw_input("Lise puan ortalamanýzý giriniz:"))

OBP=(LO*60)/100
YP=((YGSPUAN*40)/100)+((LYS*60)/100)+OBP
print"YP",YP
    













































    

