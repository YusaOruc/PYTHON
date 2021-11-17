import random
a=int(raw_input("Satýr sayýsýný giriniz:"))
b=int(raw_input("Sütun sayýsýný giriniz:"))
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
    x=int(raw_input("Seçmek istediðiniz satýr:"))
    y=int(raw_input("Seçmek istediðiniz sütun:"))
    if matris[x-1][y-1]==5:
        print "Seçili"
    elif matris[x-1][y-1]==1:
        print "BOOMMM"
        print "Puanýn:",puan
        kontrol=False
    else:
        print "Hala hayattasýn...Devam"
        matris[x-1][y-1]=5
        puan=puan+10
