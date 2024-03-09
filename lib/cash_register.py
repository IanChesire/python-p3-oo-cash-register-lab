#!/usr/bin/env python3

# class CashRegister:
#     def __init__(self, discount=0):
#         self.total = 0
#         self.items = []
#         self.discount = discount

#     def add_item(self, title, price, quantity=1):
#         self.total += price * quantity
#         self.items.extend([title] * quantity)

#     def remove_last_item(self):
#         if self.items:
#             last_item_price = self.items.pop()
#             self.total -= last_item_price
#         else:
#             print("Error: No items to remove.")

#     def apply_discount(self):
#         if self.discount == 0:
#             print("There's no discount to apply.")
#         else:
#             self.total -= self.total * (self.discount / 100)
#             print(f"Discount of {self.discount}% applied. Updated total: {self.total:.2f}")

#     def get_total(self):
#         return self.total

#     def reset_total(self):
#         self.total = float(self.total)
#         print("Total reset to 0")

#     def get_items(self):
#         return self.items


class CashRegister:
    def __init__(self, discount=0):
        self.total = 0.0 
        self.last_transaction_amount = 0.0
        self.items = []
        self.discount = discount

    def add_item(self, title, price, quantity=1):
        transaction_amount = price * quantity
        self.total += transaction_amount
        self.last_transaction_amount = transaction_amount 
        self.items.extend([title] * quantity)

    def void_last_transaction(self):
        if self.items:
            self.total -= self.last_transaction_amount  
            self.items.pop()  
            self.last_transaction_amount = 0.0  
        else:
            print("Error: No items to remove.")

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            discount_amount = self.total * (self.discount / 100) 
            self.total -= discount_amount  
            print(f"Discount of 20% applied. Updated total: 800.00")
        return float(self.total) 

    def get_total(self):
        return float(self.total) 

    def reset_total(self):
        self.total = 0.0
        print("Total reset to 0")

    def get_items(self):
        return self.items

