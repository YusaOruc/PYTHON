a=int(raw_input("Bir sayý girin:"))
b=int(raw_input("Bir sayý girin:"))
c=int(raw_input("Bir sayý girin:"))

T=b**2-4*a*c
if T>0:
    x1=(-b+T**1/2)/2*a
    x2=(-b-T**1/2)/2*a
    print "x1:",x1,"x2:",x2
elif T==0:
      X=(-b/2*a)
      print "X:",X
else:
    print "real kök yoktur"
