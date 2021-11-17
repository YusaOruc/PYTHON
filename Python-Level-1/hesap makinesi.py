import sys

while True:
    print "1.sayi="
    a=input()
    print "\n 2.sayi="
    b=input()

    print "islem: + - * / cikmak icin x:"

    op=raw_input()
    if op=="x":
        sys.exit()
    else:
        islem=str(a)+op+str(b)

        print "\n sonuc",eval(islem) #eval python ortamýnda
