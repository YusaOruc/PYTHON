import random
matris=[[0 for j in range(5)] for i in range(4)]

for i in range(4):
    for j in range(5):
        matris[i][j]=random.randint(0,1)
        
for i in range(4):
    for j in range(5):
        print matris[i][j],
    print

for i in range(4):
    for j in range(5):
        if matris[i][j]==1:
            print i,j," ",
        
