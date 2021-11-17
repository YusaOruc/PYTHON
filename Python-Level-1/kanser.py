kromozom=str(raw_input("kromozomu giriniz:"))
def kanser(kromozom):
    s = ""
    i = 0
    while i < len(kromozom):
        veri = kromozom[i:i+2]
        if veri == "00":
            s= s +"A"
        elif veri == "11":
            s= s+"T"
        elif veri == "01":
            s= s+"C"
        else:
            s= s+"G"
        i = i+2

    i=0
    while i < len(s):
        veri2 = s[i:i+4]
        if veri2 == "ATCG":
            print("Pankreas Kanseri")
            return
        elif veri2 == "ATCC":
            print("iyi Huylu Kanser")
            return
        i = i+1
    print("Kanser tehdidi yok")
    return
kanser(kromozom)

