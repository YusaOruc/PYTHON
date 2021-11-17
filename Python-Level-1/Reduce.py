
def faktoriyel(sayi1,sayi2):
    return sayi1*sayi2

sayilar = range(1,11)

print reduce(faktoriyel,sayilar)
