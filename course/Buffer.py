class Buffer:
    lst = []

    def __init__(self):
        lst = []

    def add(self, *a):
        self.lst.extend(a)
        while self.lst.__len__() >= 5:
            counter = 0
            for i in self.lst[0:5]:
                counter += i
            print(counter)
            del self.lst[0:5]

    def get_current_part(self):
        return self.lst


a = Buffer()
a.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2 ,2)
print(a.get_current_part())
a.add(1, 2, 3)
print(a.get_current_part())
