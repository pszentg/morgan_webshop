import string

from app.customer import Customer
from app.inventory import Item


class PaymentProcessor:
    def __init__(self, inventory):
        self.inventory = inventory

    def start_transaction(self, customer: Customer, item: Item, amount: int, payment_type: string):
        if self.inventory.is_on_stock(item, amount):
            # could check customer balance, etc.
            if payment_type == 'cc':
                if customer.ccDetails == 'a':
                    customer.callback("transaction went through")
                elif customer.ccDetails == 'b':
                    customer.callback("not enough funds")
                elif customer.ccDetails == 'c':
                    customer.callback("transaction failed")
            else:
                customer.callback("cash transaction")

