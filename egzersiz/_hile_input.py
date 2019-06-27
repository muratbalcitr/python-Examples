print("çıkmak için q'ye basabilirsiniz..")

toplam = 0

while True :
    value = input("sayı griniz => ")
    if value == "q" :
        print("programdan çıkılıyor...")
        break
    else :
        toplam += int(value)
print("toplam değer = > ", toplam)
