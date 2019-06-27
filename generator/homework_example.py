class Kareler() :

    def __init__(self, max) :
        self.max = max

        self.index = 0

    def __iter__(self) :
        return self

    def __next__(self) :
        if self.index <= self.max :
            sonuc = self.index ** 2
            self.index += 1

        else :
            raise StopIteration

        return sonuc


kareler = Kareler(100)

iteration = iter(kareler)

print(next(iteration))
print(next(iteration))
print(next(iteration))
print(next(iteration))

print("-------------------------------")

for i in kareler:
    print(i)