class Budget:
    def __init__(self):
        self.budget = []

    def add_item(self, it):
        self.budget.append(it)

    def remove_item(self, indx):
        del self.budget[indx]

    def get_items(self):
        return self.budget

    def __add__(self, other):
        temp = sum([x._money for x in self.budget])
        return temp + other._money

    def __radd__(self, other):
        return self + other


class Item:
    def __init__(self, name, money):
        self._name = name
        self._money = money

