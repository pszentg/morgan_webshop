import json

from customer import Customer
from inventory import Inventory, Item
from payment_processor import PaymentProcessor

inventory = Inventory()
customers = []
shopping_list = []
with open("example_data.json", "r") as f:
    items = json.load(f)
    for k, v in items['inventory'].items():
        inventory.add(Item(k), v)

    for k, v in items['customers'].items():
        customers.append(Customer(k, v))

    for k, v in enumerate(items['shopping_list']):
        amounts = items['shopping_list'][v]
        for amount in amounts:
            shopping_list.append((Item(v), amount))

payment_processor = PaymentProcessor(inventory)

for k, v in enumerate(customers):
    payment_processor.start_transaction(v, shopping_list[k][0], shopping_list[k][1])
