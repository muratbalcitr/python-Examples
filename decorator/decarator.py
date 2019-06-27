import time


def zaman_hesapla(func) :
    def wrapper(sayilar) :
        baslama = time.time()

        sonuc = func(sayilar)

        bitis = time.time()

        print(func.__name__ + " " + str(bitis - baslama) + " saniye sürdü")

        return sonuc

    return wrapper


@zaman_hesapla
def kare_hesapla(sayilar) :
    sonuc = list()

    for i in sayilar :
        sonuc.append(i ** 2)
    return sonuc


@zaman_hesapla
def kup_hesapla(sayilar) :
    sonuc = list()

    for i in sayilar :
        sonuc.append(i ** 3)
    return sonuc


kare_hesapla(range(100000))
kup_hesapla(range(100000))