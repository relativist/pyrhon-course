class MoneyBox:
    capacity = 0
    coins = 0

    def __init__(self, capacity):
        self.capacity = capacity

    def can_add(self, v):
        return self.coins + v <= self.capacity

    def add(self, v):
        if self.can_add(v):
            self.coins += v
