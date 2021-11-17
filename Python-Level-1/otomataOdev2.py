dizi=[1,1,0,1,0] 
deger=0         
i=0
ucDurum=3

print dizi
print "-------------------"
print "(q",deger,")",
for c in range(len(dizi)):
    print dizi[c],
print
    

while(i<len(dizi)):
    if deger==0 and dizi[i]==0:
        
        deger=1
        i=i+1
        for j in range(i+1):
            if (j==i):
                print "(q",deger,")",
                c=len(dizi)-j
                for a in range(i,c+1):
                    print dizi[a],
                print 
                
            else:
                print dizi[j],
        
      
    elif  deger==0 and dizi[i]==1:
        deger=2
        i=i+1
        for j in range(i+1):
            if (j==i):
                print "(q",deger,")",
                c=len(dizi)-j
                for a in range(i,c+1):
                    print dizi[a],
                print 
            else:
                print dizi[j],
                
    elif  deger==1 and dizi[i]==0:
        deger=3
        i=i-1
        for j in range(i+1):
            if (j==i):
                print "(q",deger,")",
                c=len(dizi)-j
                for a in range(i,c+1):
                    print dizi[a],
                print 
            else:
                print dizi[j],
    elif deger==1 and dizi[i]==1:
        deger=2
        i=i-1
        for j in range(i+1):
            if (j==i):
                print "(q",deger,")",
                c=len(dizi)-j
                for a in range(i,c+1):
                    print dizi[a],
                print 
            else:
                print dizi[j],
    elif  deger==2 and dizi[i]==0:
        deger=2
        i=i+1
        for j in range(i+1):
            if (j==i):
                print "(q",deger,")",
                c=len(dizi)-j
                for a in range(i,c+1):
                    print dizi[a],
                print 
            else:
                print dizi[j],
    elif  deger==2 and dizi[i]==1:
        deger=3
        i=i+1
        for j in range(i+1):
            if (j==i):
                print "(q",deger,")",
                c=len(dizi)-j
                for a in range(i,c+1):
                    print dizi[a],
                print 
            else:
                print dizi[j],
    elif  deger==3 and dizi[i]==0:
        deger=1
        i=i+1
        for j in range(i+1):
            if (j==i):
                print "(q",deger,")",
                c=len(dizi)-j
                for a in range(i,c+1):
                    print dizi[a],
                print 
            else:
                print dizi[j],
    elif  deger==3 and dizi[i]==1:
        deger=1
        i=i+1
        for j in range(i+1):
            if (j==i):
                print "(q",deger,")",
                c=len(dizi)-j
                for a in range(i,c+1):
                    print dizi[a],
                print 
            else:
                print dizi[j],
    
if(deger==ucDurum):
    print "2DFA BU DÝZÝYÝ TANIR"
else:
    print "2DFA BU DÝZÝYÝ TANIMAZ"

#HOCAM SAÐLAMASINI YAPTIM KOD ÇALIÞMAKTADIR KOLAY GELSÝN.
