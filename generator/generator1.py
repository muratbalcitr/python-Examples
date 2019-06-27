def kare_hesapla():
    for i in range(2,12):
        yield i **2

generator = kare_hesapla()

iterator = iter(generator)


print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

print("--------------------------------")
iterator2 = iter(generator)
print(next(iterator2))



print("list comp")
liste = [i*2 for i in range(10)]

generator2 = (i*2 for i in range(10))

iterator3 = iter(generator2)
print(next(iterator3))
print(next(iterator3))


print("çarpım tablosu")

def carpim_tablosu():

    for i in range(1,11):

        for j in range(1,11):

            yield "{} * {} = {}".format(i,j,i*j)

for i in carpim_tablosu():
    print(i)