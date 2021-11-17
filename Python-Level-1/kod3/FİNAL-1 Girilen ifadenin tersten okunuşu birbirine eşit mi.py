a=str(raw_input("Bir ifade giriniz:"))
j=1
for i in range(len(a)):
    if a[0][i]==a[0][-j]:
        j=j+1
        print "eþittir" 
    else:
        print "Eþit deðil"
       
