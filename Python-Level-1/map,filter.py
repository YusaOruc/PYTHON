x=range(100)

def suzgec(x):
    return x%5==0

def degis(x):
    return x*2+1

print "Filtre örneği",filter(suzgec,x)
print ("\n")
print "Map örneği",map(degis,x)
