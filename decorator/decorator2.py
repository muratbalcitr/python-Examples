def ortalama_hesapla(func):

    def wrapper(sayilar):

        tek_sayilar_toplami=0
        tek_sayilar_ortalamasi=0

        cift_sayilar_toplami=0
        cift_sayilar_ortalamasi=0

        for i in sayilar:
            if(i%2==0):
                cift_sayilar_ortalamasi+=i
                cift_sayilar_toplami+=1
            else:
                tek_sayilar_ortalamasi+=i
                tek_sayilar_toplami+=1
        print("tek sayılar ortalaması",tek_sayilar_ortalamasi/tek_sayilar_toplami)
        print("cift sayılar ortalaması",cift_sayilar_ortalamasi/cift_sayilar_toplami)
        func(sayilar)
    return wrapper

@ortalama_hesapla
def ortalamaBul(sayilar):
    toplam=0
    for sayi in sayilar:
        toplam+=sayi
    print("genel ortalama : ",toplam/len(sayilar))

ortalamaBul([1,8,78,54,664,455,54,98,79])


