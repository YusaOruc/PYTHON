a=int(raw_input("4 basamakl� bir say� giriniz:"))


birler=a%10
a=a/10
onlar=a%10
a=a/10
yuzler=a%10
a=a/10
binler=a%10
a=a/10

dizi=["bir","iki","��","d�rt","be�","alt�","yedi","sekiz","dokuz"]
dizii=["on","yirmi","otuz","k�rk","elli","altm��","yetmi�","seksen","doksan"]

print dizi[binler-1]+"bin",dizi[yuzler-1]+"y�z",dizii[onlar-1],dizi[birler-1]
