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
print liste2


s=0
for i in range(0,len(liste2)):
    if i==liste[0]:
        s=s+1

for i in range(0,len(liste2)):
    if i==liste[1]:
        s=s+1


for i in range(0,len(liste2)):
    if i==liste[2]:
        s=s+1
for i in range(0,len(liste2)):
    if i==liste[3]:
        s=s+1

for i in range(0,len(liste2)):
    if i==liste[4]:
        s=s+1

if s==0:
    print "GG"
else:
    print s,"Tane tahmininiz tuttu"
