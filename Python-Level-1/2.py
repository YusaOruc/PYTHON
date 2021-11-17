liste=[[333,"Ahmet ss",60],[222,"selim ff",30],[111,"mertik dd",70],[444,"Batuuk rr",60]]

def soru2(liste):
    toplam=0
    i=0
    while i<len(liste):
        toplam=toplam+liste[i][2]
        i=i+1
    ort=toplam/len(liste)
    sayac=0
    for i in range(len(liste)):
        if liste[i][2]>ort:
            sayac=sayac+1
    return sayac
print soru2(liste)
