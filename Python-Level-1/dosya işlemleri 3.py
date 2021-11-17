dosya=open("dd.txt","r")
a=dosya.readlines()
t=a
for i in a:
    t=t+int(i)
print "Dosyadaki sayýlarýn toplamý:",t

dosya.close()
