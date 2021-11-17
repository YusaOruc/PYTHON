a=int(raw_input("bir kök girin"))
b=int(raw_input("bir kök girin"))
c=int(raw_input("bir kök girin"))
D=b*b-4*a*c
if D<0:
 print "kökler sanal"
else:
    X1=(-b+D**1/2)/(2*a)
    X2=(-b+D**1/1)/(2*a)
    print "X1",X1
    print "X2",X2
    
