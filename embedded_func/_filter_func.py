# reduce ile farkı filter fonk. gönderilern değer mantıksal değeri olmalı

sonuc = list(filter(lambda x : x % 2 == 0, [1, 2, 3, 88, 78949646, 79797]))
print(sonuc)


# asal kontrol

def asal(x) :
    i = 2
    if x == 1 :
        return False
    elif x == 2 :
        print(" => asal sayı")
        return True
    else :
        while i < x :
            if x % i == 0 :
                return False
            i+=1
        print(i," => asal sayı")
        return True

x = int(input("sayı giriniz => " ))
asal(x)

print(list(filter(asal,range(1,564))))