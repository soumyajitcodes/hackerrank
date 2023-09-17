#!/bin/python3

import math
import os
import random
import re
import sys


class VendingMachine:
    # Implement the VendingMachine here
    def __init__(self, num_items, item_price):
        self.num_items = num_items
        self.item_price = item_coins

    def buy(self, req_items, money):
        if self.num_items >= req_items and req_items * self.item_price <= money:
            self.num_items -= req_items
            return money - (req_items * self.item_price)
        else:
            if self.num_items < req_items:
                return "Not enough items in the machine"
            else:
                return "Not enough coins"


if __name__ == "__main__":
    num_items, item_coins = map(int, input().split())
    machine = VendingMachine(num_items, item_coins)

    n = int(input())
    for _ in range(n):
        num_items, num_coins = map(int, input().split())
        try:
            change = machine.buy(num_items, num_coins)
            print(str(change) + "\n")
        except ValueError as e:
            print(str(e) + "\n")
