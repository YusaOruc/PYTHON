liste=["elma","armut","karpuz","kavun","erik","üzüm"]
while True:
    try:
        s=raw_input("Lütfen meyve adýný giriniz:")
        p=liste.index(s)+1
        print s,"Listenizde",p,"no lu sýrada bulunuyor"
    except ValueError:
        pass
