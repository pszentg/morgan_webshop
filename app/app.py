import json

from app.customer import Customer
from app.inventory import Inventory, Item

inventory = Inventory()
customers = []
with open("example_data.json", "r") as f:
    items = json.load(f)
    for k, v in items['inventory'].items():
        inventory.add(Item(k), v)

    for k, v in items['customers'].items():
        customers.append(Customer(k, v))



print(inventory.stock)
