a=[[333,"Ahmet ss",50],[222,"selim ff",30],[111,"mertik dd",70],[444,"Batuuk rr",60]]

def siraliIsimler (a):
    b=[]
    c=[]
    for i in range (0,len(a)):                 
        b.append (a[i][2])                     
        c.append (a[i][2])
    
    
    for i in range(len(b)-1,0,-1):
        enbi=0
        for j in range(1,i+1):
            if b[j]<b[enbi]:
                enbi = j

        temp = b[i]
        b[i] = b[enbi]
        b[enbi] = temp
 
    for i in range (len(b)):
        for j in range (len(b)):
            if b[i]==c[j]:
                print a[j][1]
          
siraliIsimler(a)
