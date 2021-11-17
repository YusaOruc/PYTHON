a=[[1,2,3],[4,5,6],[4,5,6]]
b=[[7,8,9],[1,2,3],[7,8,9]]
c=[[0 for j in range(3)] for i in range(3)]
for i in range(3):
    for j in range(3):
        c[i][j]=a[i][j]*b[i][j]
    print

for i in range(3):
    for j in range(3):
        print c[i][j],
    print
