dizi=[15,16,15,14,16,15,15,14]

def soru2(dizi):
    tablo=[]
    tablo.append(dizi[0])
    i=1
    while i<len(dizi):
        tablo.append(dizi[i]-dizi[i-1])
        i=i+1
    print tablo
    toplambit=len(tablo)
    for i in (tablo):
        if i<0:
            i=i*(-1)
            toplambit=toplambit+1
        while i>1:
            i=i/2
            toplambit=toplambit+1
    print toplambit
    
    
soru2 (dizi)

        
        
    




