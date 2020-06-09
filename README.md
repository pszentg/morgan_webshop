# morgan_webshop
a small demo for the Morgan Stanley interview

## Tasks
A webshop, with an inventory, which stores a list of items and their availability, handles processing the payment, 
and stores user data, etc.
The customer details are passed to the payment class, which checks if the inventory has the item(s) which the user wants to buy, 
if yes, handles the payment (cash or credit card), then calls back to the user with a status code 
(payment was ok/not enough funds/error processing the payment).
