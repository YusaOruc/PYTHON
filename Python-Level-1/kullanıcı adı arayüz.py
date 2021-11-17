from Tkinter import *
pencere=Tk()

user=Label(pencere,text="Kullanici")
passwd=Label(pencere,text="Sifre")

user.grid(row=0,column=0,sticky=E)
passwd.grid(row=1,column=0,sticky=E)

entry_1=Entry(pencere)

entry_2=Entry(pencere)

entry_1.grid(row=0,column=1)

entry_2.grid(row=1,column=1)


tik=Checkbutton(pencere,text="Beni Hatýrla")
tik.grid(columnspan=2)
pencere.mainloop()













pencere.mainloop()
