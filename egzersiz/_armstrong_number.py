
sayi = input("sayı giriniz : ")

eleman_sayisi = len(str(sayi))

toplam = 0

temp = int(sayi)
sayi2 =int(sayi)
while temp>0:

    digit = temp %10

    toplam += digit**eleman_sayisi
    print(digit**eleman_sayisi ," =>", toplam)
    temp //=10

if(sayi2 == toplam):
    print(sayi,"amstrong sayı")
else:
    print(sayi, "amstrong sayı değildir")