a=int(raw_input("4 basamaklý bir sayý giriniz:"))


birler=a%10
a=a/10
onlar=a%10
a=a/10
yuzler=a%10
a=a/10
binler=a%10
a=a/10

dizi=["bir","iki","üç","dört","beþ","altý","yedi","sekiz","dokuz"]
dizii=["on","yirmi","otuz","kýrk","elli","altmýþ","yetmiþ","seksen","doksan"]

print dizi[binler-1]+"bin",dizi[yuzler-1]+"yüz",dizii[onlar-1],dizi[birler-1]
