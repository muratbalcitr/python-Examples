


print("bir sat-yının faktoriyelini bulma....")

while True:
    sayi = input("sayı giriniz : ")
    if sayi =="q":
        x = input("çıkmak için (1) devam etmek için (2) yi tıklayın")
        if x =="1":
            break
        else:
            continue
    elif sayi=="":
        continue

    else:
        sayi = int(sayi)
        fakt =1

        for i in range(2,sayi+1):
            fakt *=i
        print(fakt)