x=range(100)

def suzgec(x):
    return x%5==0

def degis(x):
    return x*2+1

print "Filtre ?rne?i",filter(suzgec,x)
print ("\n")
print "Map ?rne?i",map(degis,x)
