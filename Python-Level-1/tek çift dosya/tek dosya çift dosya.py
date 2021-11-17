a=open("çift.txt","a")
b=open("tek.txt","a")
for i in range(100):
    if i%2==0:
        a.write(str(i)+","),
    else:
        b.write(str(i)+","),
        
a.close()
b.close()
