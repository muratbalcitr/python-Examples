# reduce sol baştan başlayarak önce ilk 2 elemana uyguluyor
#çıkan sonucu 3. elemana uyguluyor ve liste bitince 1 değer dönüyor

from functools import reduce


def double(sayi,sayi2):
    return sayi*sayi2

toplam = reduce(double,[12,13,14,15])
print(toplam)

#########################3

print(reduce(lambda x,y : x*y,[1,3,4,5,6]))

########listenin en büyük sayısını bulma ##############

def maximum(x,y):
    if x>y:
        return x
    else:
        return y

enb = reduce(maximum,[12,434,122134,324543657,234234,123,1314141,14151451])
print(enb)









