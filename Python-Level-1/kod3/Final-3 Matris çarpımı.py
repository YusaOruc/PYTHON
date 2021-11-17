import random
matris=[[0 for j in range(10)] for i in range(10)]
matris1=[[0 for j in range(10)] for i in range(10)]
matris2=[[0 for j in range(10)] for i in range(10)]
for i in range(10):
    for j in range(10):
        matris[i][j]=random.randint(0,9)

for i in range(10):
    for j in range(10):
        matris1[i][j]=random.randint(0,9)        

for i in range(10):
    for j in range(10):
        matris2[i][j]=matris[i][j]*matris1[i][j]

for i in range(10):
    for j in range(10):
        print matris[i][j],
    print
print

for i in range(10):
    for j in range(10):
        print matris1[i][j],
    print
print
for i in range(10):
    for j in range(10):
        print matris2[i][j],
    print
