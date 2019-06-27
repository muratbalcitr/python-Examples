def main_func(islem_adi) :
    def toplama(*args) :
        toplam = 0
        for i in args :
            toplam += i
        return toplam

    def carpim(*args) :
        carpim_ = 0
        for i in args :
            carpim_ *= i
        return carpim_

    def bolme(*args) :
        bolme_ = 0
        for i in args :
            bolme_ /= i
        return bolme_

    def cikarma(*args) :
        cikarma_ = 0
        for i in args :
            cikarma_ -= i
        return cikarma_

    if islem_adi == "toplama" :
        #return toplama
        print(toplama(1,2))
    elif islem_adi == "cikarma":
        print(cikarma(2,4))
    elif islem_adi == "bolme":
        print(bolme(10,5))
    else :
        print(carpim(2,3))


fonk = main_func("bolme")
print(fonk)
