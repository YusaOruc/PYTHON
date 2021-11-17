i=0
dizi=[]
while i<4:
    a=int(raw_input("Bir sayý giriniz:"))
    dizi.append(a)
    i=i+1
def soru2(dizi):
    t=len(dizi)
    for i in(dizi):
        while i>1:
            i=i/2
            t=t+1
    print t
soru2(dizi)

