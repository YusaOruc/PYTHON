a=int(raw_input("Bir say� giriniz:"))
b=int(raw_input("Bir say� giriniz:"))
i=1
ebob=0
while i<=a:
    
    if a%i==0 and b%i==0:
        if ebob<i:
            ebob=i
    i=i+1
print "Ebob:",ebob
