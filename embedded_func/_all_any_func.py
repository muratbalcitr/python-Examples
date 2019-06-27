

def all_(liste):
    for i in liste:
        if not i:
            return False
    return True

liste = [True,False,False,True,False,False]

print(all_(liste))

#all() metodu en az bir değer false ise false sonucunu döndürür

sonuc = all(liste)
print("all() => ",sonuc)

#any() fonksiyonu en az bir true var ise true döndürür
sonuc2 =any(liste)
print("any() =>",sonuc2)
