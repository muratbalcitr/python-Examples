

sayi = int(input("sayı giriniz : "))

liste = []
toplam =0
for i in range(1,sayi):
    if(sayi%2==0):
        toplam +=i
if(sayi == toplam):
    print("mükemmel sayı")
else:
    print("mükemmel sayı değil")


