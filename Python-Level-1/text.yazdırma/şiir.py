dosya=open("þiir.txt","w")
dosya.write("Bütün güneþler batmadan,\nBi türkü daha söyleyeyim bu yerde")
dosya.close
with open("þiir.txt","r")as dosya:
    a=dosya.read()
    print a

    #dosyayý basa sarma    
    dosya.seek(0)
    b=dosya.read()
    print b

    #dosyanýn basýna veri ekleme
with open("þiir.txt","r+")as f:
    veri=f.read()
    f.seek(0)
    f.write("Selim özden\t:0212 222 22\n"+veri)

    #Ýstediðin satýra ekleme    
with open("þiir.txt","r+")as f:
    veri=f.read()
    f.insert("2","Sedat Köz\t:25051522525")
    f.writelines(veri)
