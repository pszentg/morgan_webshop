# Webshop demo
a small webshop demo

## Tasks
A webshop, with an inventory, which stores a list of items and their availability, handles processing the payment, 
and stores user data, etc.
The customer details are passed to the payment class, which checks if the inventory has the item(s) which the user wants to buy, 
if yes, handles the payment (cash or credit card), then calls back to the user with a status code 
(payment was ok/not enough funds/error processing the payment).

## Installation
The project doesn't have any specific dependencies other than python 3.8 and pip

## Usage
`python3 app.py` runs the example. You can add example data entries to `example_data.json`. Make sure that the amount of customer entries match the
number of items on the shopping list. The shopping list stores lists of instances the items will be requested by a customer,
so `"Guitar": [2,2]` means 2 Guitars will be purchased by 2 different customers.

Assign `null` to the customer ID if you want a cash transaction. Else you can use any string.