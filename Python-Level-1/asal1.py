x=int(raw_input("Bir sayý giriniz:"))
for i in range (2,x-1):
    if x%i==0:
        break
    else:
        print i
