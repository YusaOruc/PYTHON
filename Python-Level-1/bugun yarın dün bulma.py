import datetime

bugun=datetime.datetime.today()

fark=datetime.timedelta(weeks=0,days=1,minutes=0,seconds=0)

yarin=bugun+fark
dun=bugun-fark

ikigunoncesi=bugun-fark*2

print bugun
print yarin
print dun
print ikigunoncesi
