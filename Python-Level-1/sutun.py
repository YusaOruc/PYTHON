liste=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
def soru(liste):
    i=0
    s=0
    while i<len(liste):
        print liste[i][s],
        i=i+1
        if i==4:
            i=0
            s=s+1
            if s==4:
                return
soru(liste)
