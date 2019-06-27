class Command() :
    def __init__(self, channelList) :
        self.channelList = channelList
        self.index = -1

    def __iter__(self) :
        return self

    def __next__(self) :
        self.index += 1
        if (self.index < len(self.channelList)) :
            return self.channelList[self.index]
        else :
            self.index = -1
            raise StopIteration


command = Command(["atv", "kanald", "star", "tv8"])

iterator = iter(command)  # Objemiz iterable olduğu için iterator oluşturulabilir.
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
