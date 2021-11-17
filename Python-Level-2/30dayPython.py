#kelime=input("Bir kelime girin :")
#sayilar = {"1": "bir", "2": "iki", "3": "üç", "4": "dört", "5": "beş"}
#if(kelime in sayilar):
    #print(sayilar[kelime])
#else:
    #print(("gg"))
#print(sayilar.keys())
#-----------------------------------------------------------
'''''
bag=[0,5,3,5.25,6,"dfsdf","sdgfsdfg","sdf"]
def parse_liste(some_list):
    intdegerler=[]                                 
    stringdegerler=[]                              
    floatdegerler=[]                               
    for rnd in some_list:
        if isinstance(rnd,int):                    
            intdegerler.append(rnd)                
        elif isinstance(rnd,float):                
            floatdegerler.append(rnd)              
        elif isinstance(rnd,str):                  
            stringdegerler.append(rnd)             
    print(intdegerler,stringdegerler,floatdegerler)
parse_liste(bag)
'''''
#-----------------------------------------------------------
import datetime
import random

''''' 
import random
liste=[]
for i in range(0,10):
    a=random.randint(0,100)
    liste.append(a)
print(liste)
b=0
k=101
toplam=0
for item in liste:
    toplam=toplam+item
    if(b<item):
        b=item
    elif(k>item):
        k=item
toplam=toplam/len(liste)
print("Büyük:",b )
print("Küçük:",k)
print("Ortalama",toplam)
'''''
#-----------------------------------------------------------
'''''
matris=[[0 for j in range(5)]for i in range(5)]
for i in range(5):
    for j in range(5):
        matris[i][j]=random.randint(0,9)
for i in range(5):
    for j in range(5):
        print(matris[i][j],end=" ")
    print()
satir=0
satirListesi=[]
sutun=0
sutunListesi=[]
for i in range(5):
    for j in range(5):
        satir=satir+matris[i][j]
        sutun=sutun+matris[j][i]
        if j == 4:
            satirListesi.append(satir)
            sutunListesi.append(sutun)
            satir = 0
            sutun=0
print(satirListesi)
print(sutunListesi)
'''''
#-----------------------------------------------------------
'''''
"this cool {name}".format(name='justin')
print("this cool {name}\n right?".format(name='justin'))
"Hi %s whats up!!"%("Justin")
print("Hi %s whats up!!"%("Justin"))
'''''
#-----------------------------------------------------------
'''''
default_names=["Justin","Tom","Brad","Eric"]
default_amounts=[123,2569.5,2556,2541.5]
unf_message="""Hi {name}!
Thank you for the purchase on {date} 
We hope you are exicted about using it.
Just as a reminder the purcase total was ${total}
Hava great one !
Team Arien
"""
def make_massages(names,amounts):
    messages=[]
    if (len(names)==len(amounts)):
        i=0
        today=datetime.date.today()
        text='{today.month}/{today.day}/{today.year}'.format(today=today)
        for name in names:
            new_amount=amounts[i]
            new_msg=unf_message.format(name=name,
                                       date=text,
                                       total=new_amount)
            i=i+1
            print(new_msg,"fg")

make_massages(default_names,default_amounts)
'''''
#-----------------------------------------------------------
'''''
class Animal():
    name="Amy"
    noise="Grunt"
    size="Large"
    color="brown"
    hair="Covers bady"
    print("dsfsfd")
    def get_color(self):
        return self.color
    def make_noise(self,abc):
        return self.noise+" "+abc


dog=Animal()

print(dog.get_color())
print(dog.make_noise("red"))


class Dog(Animal):
    name = "Jon"
    size = "small"
    color = "black"
    age=19
    def get_color(self):
        return self.color
jon=Dog()
jon.color='white'
jon.name='Jon Snow'
print(jon.get_color())
'''''
#-----------------------------------------------------------













