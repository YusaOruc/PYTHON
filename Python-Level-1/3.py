liste=[[333,"hmet ss",70],[222,"belim ff",80],[111,"bertik dd",81],[444,"atuuk rr",90]]
def soru3(liste):
    ek=101
    i=0
    satir=-1
    while i<len(liste):
        if liste[i][1][0:1]=="b":
            if ek>liste[i][2]:
                ek=liste[i][2]
                satir=i
    
        i=i+1
  
      
    return liste[satir][0]


print soru3(liste)
