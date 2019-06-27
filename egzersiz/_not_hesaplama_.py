def hesapla(satir) :
    liste = satir[: :-1]
    liste = satir.split(",")
    print(liste)
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])
    sonuc = not1 * (3 / 10) + not2 * (3 / 10) + not3 * (4 / 10)
    if sonuc >= 90 :
        harf = "AA"

    elif sonuc >= 85 :
        harf = "BA"

    elif sonuc >= 80 :
        harf = "BB"

    elif sonuc >= 75 :
        harf = "CB"

    elif sonuc >= 70 :
        harf = "CC"
    elif sonuc >= 65 :
        harf = "DC"
    elif sonuc >= 60 :
        harf = "DD"

    elif sonuc >= 55 :
        harf = "DF"
    else :
        harf = "FF"
    return liste[0] + " ----- >" + harf


def gec_kal(satir) :
    liste = satir[: :-1]
    liste = satir.split(",")
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])
    sonuc = not1 * (3 / 10) + not2 * (3 / 10) + not3 * (4 / 10)
    #if sonuc >= 55 :
    #    durum = "geçti"
    #else :
    #    durum = "kaldı"
    return sonuc


with open("ogrenciler.txt", "r", encoding="utf-8") as file :
    eklenecekler = []
    kalanlar = []
    gecenler = []
    for i in file :
        eklenecekler.append(hesapla(i))
    print(eklenecekler)


def file_create(file_name, liste) :
    with open(file_name + ".txt", "w", encoding="utf-8") as gec_kal_file :
        print(liste)
        for i in liste :
            gec_kal_file.write(liste[0],i)
        print(liste)


with open("ogrenciler.txt", "r+", encoding="utf-8") as file2 :
    for i in file2 :
        # kalanlar.append(i)
        sonuc = gec_kal(i)
        if sonuc >= 55 :
            gecenler.append(gec_kal(i))
            file_name = "gecen_ogrenci"
            file_create(file_name, gecenler)
        else :
            kalanlar.append(gec_kal(i))
            file_name = "kalan_ogrenci"
            file_create(file_name, kalanlar)
