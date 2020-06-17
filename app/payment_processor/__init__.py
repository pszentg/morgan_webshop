class PaymentProcessor:
    def __init__(self, inventory):
        self.inventory = inventory

    def start_transaction(self, customer, item, amount: int):
        if self.inventory.is_on_stock(item, amount):
            # could check customer balance, etc.
            if customer.ccDetails == 'a':
                customer.callback("transaction went through")
                self.inventory.remove(item, amount)
            elif customer.ccDetails == 'b':
                customer.callback("not enough funds")
            elif customer.ccDetails == 'c':
                customer.callback("transaction failed")
            elif customer.ccDetails is None:
                customer.callback("cash transaction")
        else:
            customer.callback("not enough items are on stock")
