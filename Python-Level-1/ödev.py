import random
matris=[[0 for j in range(10)]for i in range(10)]
for i in range(10):
    for j in range(10):
        matris[i][j]=random.randint(1,9)

for i in range(10):
    for j in range(10):
        print matris[i][j],
    print


for i in range(10):
    for j in range(i+1):
        print matris[i][j],
    print
        

    
