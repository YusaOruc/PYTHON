alfabe=["a","b","c","d","e","f","i","j","o"]
def filtersesli(alfabe):
    sesliler=["a","e","i","o","u"]
    if(alfabe in sesliler):
        return True
   
        return False

filtersesli=filter(filtersesli,alfabe)
print("Filtrelenen sesli harfler:")
print (filtersesli)
