liste=["Python","Ruby","pHp","JAVA","scala","go"]

def suz(x):
    return x.istitle()

def cevir(x):
    return x.capitalize()

print filter(suz,liste)
print map(cevir,liste)
