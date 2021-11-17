
liste=[[333,"Ahmet ss",50],[222,"selim ff",90],[111,"mertik dd",91],[444,"Batuuk rr",10]]
def soru1 (liste):
    satir=0
    i=0
    enbuyuk=0
    while i<len(liste):
        if enbuyuk<liste[i][2]:
            enbuyuk=liste[i][2]
            satir=i
        i=i+1
    yeni=liste[satir][1].split(" ")
    return yeni [-1]

print soru1(liste)
