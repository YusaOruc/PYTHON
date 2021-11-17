import random
dosya=open("dd.txt","w")
harf="qwertyuýopðüiþlkjhgfdsazcvnmöç"
for i in range(25):
    dosya.write(str(random.choice(harf))+"="+str(random.randint(0,10))+"\n")
    

dosya.close()
