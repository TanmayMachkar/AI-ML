a = ["Tanmay", "TusharGandu", "TusharGod", "Tejas"]
itr = iter(a)
print(next(itr))

#reversed
itr1 = reversed(a)
print(next(itr1))

class RemoteControl():
    def __init__(self):
        self.channels = ["StarTv", "HBO", "abc", "espn"]
        self.index = -1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration
        return self.channels[self.index]
    
r = RemoteControl()
itr = iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))