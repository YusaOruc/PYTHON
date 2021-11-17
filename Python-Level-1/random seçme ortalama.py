import random
x=[]
toplam=0
for i in range(10):
    a=random.randint(0,100)
    x.append(a)
    toplam+=a
print x
print "ortalama:",toplam/len(x)

enb=0
for s in range(len(x)):
    if enb<x[s]:
        enb=x[s]
print "En büyük:",enb


enk=101
for j in range(len(x)):
    if enk>x[j]:
        enk=x[j]
    
print "En küçük:",enk
    

    
