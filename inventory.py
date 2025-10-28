"""
Inventory management system module.
Handles adding, removing, saving, and loading inventory data.
Includes basic logging.
"""


import json  # removed import logging since it was never used
from datetime import datetime
import ast


stock_data = {}


def add_item(item="default", qty=0, logs=None):  # renamed from addItem
    """
    Add a given quantity of an item to the stock dictionary
    """
    if logs is None:
        logs = []
    stock_data[item] = stock_data.get(item, 0) + qty
    # changed to f-string
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):  # renamed from removeItem
    """
    Remove an item or decrease its quantity from the stock.
    """
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:  # changed from Exception to KeyError
        pass


def get_qty(item):  # renamed from getQty
    """
    Return the quantity of the given item from stock_data.
    """
    return stock_data[item]


def load_data(file="inventory.json"):  # renamed from loadData
    """
    load the data from inventory
    """
    with open(file, "r", encoding="utf-8") as f:  # fixed: added encoding
        data = json.loads(f.read())
    return data


def save_data(file="inventory.json"):   # renamed from saveData
    """
    save the data
    """
    with open(file, "w", encoding="utf-8") as f:
        f.write(json.dumps(stock_data))


def print_data():  # renamed from printData
    """
    prints the data
    """
    print("Items Report")
    for item, qty in stock_data.items():
        print(item, "->", qty)


def check_low_items(threshold=5):  # renamed from checkLowItems
    """
    checks the low items in stock data
    """
    result = []
    for item, qty in stock_data.items():
        if qty < threshold:
            result.append(item)
    return result


def main():
    """
    Main function to demonstrate inventory operations.
    """
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    stock_data.update(load_data())
    print_data()
    # fixed: replaced eval with literal_eval
    ast.literal_eval("print('eval used')")


main()
