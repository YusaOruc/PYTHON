kontrol=True
while kontrol:
    x=int(raw_input("Sayý deðerini giriniz"))
    if 1<=x<=365:
        a=x%7
        if a==0:
            print "Cumartesi"
        elif a==1:
            print "Pazar"
        elif a==2:
            print "Pazartesi"
        elif a==3:
            print "Salý"
        elif a==4:
            print "Çarþamba"
        elif a==5:
            print "Perþembe"
        elif a==6:
            print "Cuma"
        kontrol=False
    else:
        print "Tekrar deneyiniz"
              
