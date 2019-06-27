def ekstra(fonk) :
    def ekstra_ozellik() :
        print("Mükemmel Sayılar...")
        for sayi in range(1, 1001) :
            toplam = 0
            i = 1
            while (i < sayi) :
                if (sayi % i == 0) :
                    toplam += i
                i += 1
            if (toplam == sayi) :
                print(sayi)
        fonk()

    return ekstra_ozellik


@ekstra
def asal_sayi() :
    liste = list()

    for i in range(2, 1000) :

        bulundu = False

        for j in range(2, i) :
            if i % j == 0 :
                bulundu = True
                liste.append(j)
                break
        if bulundu == False :
            print(i)


asal_sayi()
