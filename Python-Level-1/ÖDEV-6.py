
a=str(raw_input("Tarihi giriniz:"))

b=str(raw_input("Günün önemini giriniz:") )

haftalar=["","","","Mart 2018","","","","Pt","Sa","Ca","Pe","Cu","Ct","Pa","        ",1,"",2,"",3,"",4,5,6,7,8,9,10,11,12,13
          ,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,""]
matris=[[0 for j in range(7)] for i in range(7)]
d=0


for i in range(7):
    for j in range(7):
        matris[i][j]=haftalar[d]
        d=d+1
        

for i in range(7):
    for j in range(7):
        print matris[i][j],
    print

    

print a,b
