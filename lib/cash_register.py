#!/usr/bin/env python3

class CashRegister:

    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []

    def add_item(self, item:str, price:int, quantity=1):
        for x in range(quantity):
            # 0 to range-1
            self.items.append(item)
        
        self.total += (price * quantity)
        self.last_item = {
            "item": item,
            "quantity": quantity,
            "price": price
        }

    def apply_discount(self):
        if self.total != 0: 
            self.total = int(self.total * (100 - self.discount) / 100)
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.items = self.items[0:len(self.items)-self.last_item["quantity"]]
        print(self.items)
        self.total -= (self.last_item["price"] * self.last_item["quantity"])
    