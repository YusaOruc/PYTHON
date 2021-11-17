a=str(raw_input("Bir parametre giriniz:"))
t=0
i=0
while i<len(a):
    if t<a.count(a[i]):
        t=a.count(a[i])
        harf=a[i]
    i=i+1

print harf,"harfinden",t,"adet vardýr."

    
