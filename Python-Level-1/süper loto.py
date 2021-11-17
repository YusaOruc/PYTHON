import random
liste=[]
liste2=[]
for i in range(0,5):
    a=int(raw_input("Tahmininizi giriniz:"))
    liste.append(a)
print "Tahminler:",liste

for i in range(0,15):
    b=random.randint(0,49)
    liste2.append(b)
print "Loto:",liste2


s=0
for i in range(0,len(liste)):
    for j in range(0,len(liste2)):
        if liste[i]==liste2[j]:
            s=s+1


print s
