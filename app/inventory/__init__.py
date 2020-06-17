import string


class Item:
    def __init__(self, item_id: string):
        self.id = item_id


class Inventory:
    def __init__(self):
        self.stock = {}

    def add(self, item, amount: int):
        try:
            self.stock[item.id] += amount
        except KeyError:
            self.stock[item.id] = amount

    # should be handled more nice
    def remove(self, item, amount=1):
        self.stock[item.id] -= amount

    # could also return the amount of stock if not enough available
    # I assumed the customer doesn't want the stock if it's not enough
    def is_on_stock(self, item, amount):
        if self.stock[item.id] > amount:
            return True
        return False
