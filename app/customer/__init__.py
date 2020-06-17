import string


class Customer:
    def __init__(self, customer_id, cc_details):
        self.id = customer_id
        self.ccDetails = cc_details

    def callback(self, transaction_status: string):
        print(f'customer {self.id} got called back with transaction status:{transaction_status}')