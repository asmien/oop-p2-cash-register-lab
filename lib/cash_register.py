#!/usr/bin/env python3


class CashRegister:
    def __init__(self, discount=0):
        # validate discount
        if isinstance(discount, int) and 0 <= discount <= 100:
            self.discount = discount
        else:
            print("Not valid discount")
            self.discount = 0

        # initialize totals and storage
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        # add to total
        self.total += price * quantity

        # add items individually (for multiples)
        for _ in range(quantity):
            self.items.append(item)

        # store transaction
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        # no discount
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        # apply percentage discount
        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount

        # format if whole number
        if self.total.is_integer():
            self.total = int(self.total)

        print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        # nothing to void
        if not self.previous_transactions:
            return

        # get last transaction
        last = self.previous_transactions.pop()

        # subtract from total
        self.total -= last["price"] * last["quantity"]

        # remove items from list
        for _ in range(last["quantity"]):
            self.items.pop()

        # prevent negative float weirdness
        if self.total < 0:
            self.total = 0.0
