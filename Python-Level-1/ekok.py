a=int(raw_input("Bir sayý giriniz:"))
b=int(raw_input("Bir sayý giriniz:"))
x=0
if a==b:
    print "ekok:",a
elif a<b:
    x=b
else:
    x=a
ekok=(a*b)+2
i=(a*b)+1
while i>0:
    if i%a==0 and i%b==0:
        if ekok>i:
            ekok=i
    i=i-1
print "Ekok:",ekok
    
