liste=[1,5,1,1,1,3,7,8,9,41,25,65]
print liste.index(41)  #Kaçıncı sırada olduğunu yazdırır.

liste.insert(3, 74) # yeni elemanı belirtilen indise ekler
print liste

liste.sort()              # listeyi sıralar
liste.reverse()           # listeyi ters çevirir
liste.pop()               # son elemanı siler
liste.append(5)           # sonuna yeni eleman ekler

liste.count(1)            # Bu eleman listede kaç tane var
del liste[2]                 # 2.indisteki elemanı listeden sil


print liste
