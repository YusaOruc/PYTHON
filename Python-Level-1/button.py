from Tkinter import *

pencere=Tk()

cerceve1=Frame(pencere)
cerceve1.pack()


cerceve2=Frame(pencere)
cerceve2.pack(side=BOTTOM)


cerceve3=Frame(pencere)
cerceve3.pack(side=BOTTOM)


button1=Button(cerceve1,text="Button1",fg ="red",)
button2=Button(cerceve1,text="Button2",fg ="red")
button3=Button(cerceve2,text="Button3",fg ="purple")
button4=Button(cerceve2,text="Button4",fg ="purple")

button5=Button(cerceve3,text="Button5",fg ="green")
button6=Button(cerceve3,text="Button6",fg ="green")


button5.pack(side=LEFT)
button6.pack(side=LEFT)




button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)
pencere.mainloop()














pencere.mainloop()
