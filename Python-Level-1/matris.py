import random
liste=[]
sayi=0
satir=input("Satırı giriniz:")
sutun=input("Sütunu giriniz:")
matris=[[0 for j in range(sutun)] for i in range(satir)]

for i in range(satir):
    for j in range(sutun):
        matris[i][j]=random.randint(0,9)
        sayi+=1
        

for i in range(satir):
    for j in range(sutun):
        print (matris[i][j],)
    print()
