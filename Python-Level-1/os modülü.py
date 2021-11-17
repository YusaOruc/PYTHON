#os modülünü incele internetten 
import os   


print os.getcwd()
print os.chdir("/") #kök dizimine götürür
print os.getcwd()

for i in os.listdir(os.getcwd()):
    if os.path.isfile(i):
        print "Dosya=>",i
    else:
        print "Klosor=>",i


