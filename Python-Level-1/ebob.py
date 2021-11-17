a=int(raw_input("Bir sayý giriniz:"))
b=int(raw_input("Bir sayý giriniz:"))
i=1
ebob=0
while i<=a:
    
    if a%i==0 and b%i==0:
        if ebob<i:
            ebob=i
    i=i+1
print "Ebob:",ebob
