from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL,"")

now = datetime.now()

print(now.year)
print(now.month)
print(now.day)
print(now.microsecond)

print(datetime.ctime(now))

print("strftime() yıl alma : ",datetime.strftime(now,"%y" ))

print("strftime() tarih alma : ",datetime.strftime(now,"%D"))

print("date fonk : ",datetime.strftime(now,"%Y, %B ,%A"))

print("TİMESPAN")

second = datetime.timestamp(now)

print("Now to second : ",second)

secondToNow  = datetime.fromtimestamp(second)

print("Second to now : " ,secondToNow)


print("tarih farkı alma")

tarih = datetime(2019,12,1)

tarih2 = datetime.now()

print(tarih-now)



