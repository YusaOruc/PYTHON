matris=[[1,2,3],[4,5,6],[7,8,9]]
t=0
for i in range(3):
    for j in range(3):
        t=t+matris[i][j]
    satir=t/3
    t=0
    print "Satýr",i+1,"in ortalamasý",satir
