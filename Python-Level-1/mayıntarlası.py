import random
a=int(raw_input("Sat�r say�s�n� giriniz:"))
b=int(raw_input("S�tun say�s�n� giriniz:"))
matris=[[0 for j in range(b)]for i in range(a)]
liste=(0,1)
for i in range(a):
    for j in range(b):
        matris[i][j]=random.choice(liste)

for i in range(a):
    for j in range(b):
        print matris[i][j],
    print
puan=0
kontrol=True
while(kontrol==True):
    x=int(raw_input("Se�mek istedi�iniz sat�r:"))
    y=int(raw_input("Se�mek istedi�iniz s�tun:"))
    if matris[x-1][y-1]==5:
        print "Se�ili"
    elif matris[x-1][y-1]==1:
        print "BOOMMM"
        print "Puan�n:",puan
        kontrol=False
    else:
        print "Hala hayattas�n...Devam"
        matris[x-1][y-1]=5
        puan=puan+10
