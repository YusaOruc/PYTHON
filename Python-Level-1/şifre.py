kontrol=True
i=1
while kontrol:
    a=int(raw_input("Þifreyi giriniz"))
    if a==123:
        print "Hoþgeldiniz"
        kontrol=False
    elif i<3:
        print"tekrar deneyiniz"
        i=i+1
    else:
        print "bloke"
        kontrol=False
     
        
