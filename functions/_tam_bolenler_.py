


def tambolenlerbulma(sayi):
    tam_bolenler_liste= []
    for i in range(2,sayi):
        if sayi % i ==0:
            tam_bolenler_liste.append(i)
    return tam_bolenler_liste


while True:
    sayi = input("sayi : ")
    if sayi == "q":
        print("program sonlanıyor...")
    else:
        sayi = int(sayi)
        print("tam bolenler : ",tambolenlerbulma(sayi))