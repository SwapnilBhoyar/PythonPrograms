"""
@Author: Swapnil Bhoyar
@Date: 2021-07-02 
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-03 01:21:00
@Title : This program implement inventory management system
"""
# importing important modules
import json
from RegexPattern import RegexPattern
from InventoryLogger import logger
import re

data = json.load(open("InventoryData.json", "r"))   # opening the JSON file and reading it and after reading the whole JSON
# file converting it to the Dictionary object


def inventory_detail(inventory_name):
    """
    Descripton:
        this method add the particular grain type after getting all the details regarding that grain
    """
    global weight_, price, name  # globalizing the variables
    try:
        while True:
                name = input("Enter the", inventory_name, " name:")
                if(re.match(re.compile(RegexPattern.NAME_PATTERN), name)):
                    break
                else:
                    logger.info("name entered is not valid")
        while True:
                price = input("Enter the price:")
                if(re.match(re.compile(RegexPattern.NAME_PATTERN), price)):
                    break
                else:
                    logger.info("price entered is not valid")
        while True:
                weight_ = input("Enter the price:")
                if(re.match(re.compile(RegexPattern.WEIGHT_PATTERN), weight_)):
                    break
                else:
                    logger.info("weite entered is not valid")
        print("\nSaving Data.....\n"
              "Data successfully Saved\n")
    except Exception as e:  # handling the exception of bad input
        logger.error(e)

    amount = int(price * weight_)  # finding the total amount and casting it in integer
    obj1 = Inventory(name, price, weight_, amount, inventory_name)  # creating object of Inventory through constructor
    obj1.update_inventory()  # writing newly created object of grain


def sell_item(item, weight, choice):
    """
    Descripton:
        this method is used to sell the selected grain with user-input of @param item, @param weight and @param choice
    """

    last_weight = data["inventory"][item][choice-1]['weight']  # storing initial weight to a new variable
    if data["inventory"][item][choice-1]['weight'] - weight > 0:  # checking whether the amount user buying is available
        # or not
        data["inventory"][item][choice-1]['weight'] -= weight  # if available then deduct the sold value from the
        # JSON file
    else:
        print("\nYou don't have sufficient amount of ", item)

    with open("InventoryData.json", "w") as inventory_data:  # writing the modified data to JSON file with proper indentation
        json.dump(data, inventory_data, indent=2, sort_keys=True)
    print("\nWeight of", data["inventory"][item][choice-1]['Name'], item, "updated from", last_weight, "to",
          last_weight - weight)
    print("\n>> Total amount :", weight * data["inventory"][item][choice - 1]['Price'], '<<\n')


def purchase_item(item, weight, choice):
    """
    Descripton:
        this method is used to purchase the selected grain with user-input of @param item, @param weight and @param choice
    """
    last_weight = data["inventory"][item][choice-1]['weight']  # storing initial weight to a new variable
    data["inventory"][item][choice-1]['weight'] += weight  # adding the purchased value to the JSON file to the
    # respective grain

    with open("InventoryData.json", "w") as inventory_data:  # writing the modified data to JSON file with proper indentation
        json.dump(data, inventory_data, indent=2, sort_keys=True)
    print("\nWeight of", data["inventory"][item][choice-1]['Name'], item, "updated from", last_weight, "to",
          last_weight + weight)
    print("\n>> Total amount :", weight * data["inventory"][item][choice - 1]['Price'], '<<\n')


# 'Inventory' class
class Inventory:
    """
    Descripton:
        custom constructor to initialize the values
    """
    def __init__(self, name, price, weight, amount, inventory_name):
        self.name = name
        self.price = price
        self.weight = weight
        self.amount = amount
        self.inventory_name = inventory_name

    def update_inventory(self):
        """
        Descripton:
            this method write data to JSON file
        """
        data["inventory"][self.inventory_name].append({
            "Name": self.name,
            "Price": self.price,
            "weight": self.weight,
        })
        with open("InventoryData.json", "w") as inventory_data:  # writing the data to the JSON file with proper indentation
            json.dump(data, inventory_data, indent=2, sort_keys=True)