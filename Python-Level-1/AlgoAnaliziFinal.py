dizi=[8,6,5,0,4,1,2,3,7,5]
i=0
a=0
sayac=0
j=0

while i<len(dizi):  
    sayi=dizi[j]
    deger=dizi[sayi]
    if deger==dizi[a]:
        sayac=sayac+1
        print sayac
        a=a+1
        j=sayac
        
        
        i=0
    else:
        j=sayi
        i=i+1
