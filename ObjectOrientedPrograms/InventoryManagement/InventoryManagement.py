"""
@Author: Swapnil Bhoyar
@Date: 2021-07-02 
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-03 01:21:00
@Title : This program implement inventory management system
"""
# importing important modules
from Inventory import *
from InventoryLogger import logger
from RegexPattern import RegexPattern
import re


def display_inventory():
    """
    Description:
        this function display all the data present in the JSON file after converting it to the Dictionary
    """
    global type  # globalizing the variable 'type'
    for i in range(len(data['inventory'])):
        # assigning the type of grain name according the index of dictionary
        if i == 0:
            type = "Rice"
        if i == 1:
            type = "Pulse"
        if i == 2:
            type = "Wheat"

        # printing the details of all the grains after accessing the Dictionary of converted JSON file
        print("\nGrain Type: ", type, "\n-------------------")
        for j in range(len(data['inventory'][type])):  # traversing throughout the Dictionary and accessing the elements
            print("Name: ", data['inventory'][type][j]['Name'])
            print("Weight: ", data['inventory'][type][j]['weight'])
            print("Price per kg: ", data['inventory'][type][j]['Price'])
            print("Total Price: ", (data['inventory'][type][j]['weight']) * (data['inventory'][type][j]
                  ['Price']))
            print()


def buy_item():
    """
    Description:
        this function is using to buy the grain from the Inventory which will reflect the amount purchased in the JSON file
    """
    print("\nChoose the item to purchase and add to Inventory\nPress 1 to purchase Rice\nPress 2 to "
          "purchase pulses\nPress 3 to purchase wheat\n")  # displaying sub-menu
    try:
        while True:
                choice = int(input("Enter your opinion: "))
                if(re.match(re.compile(RegexPattern.NUMBER_PATTERN), choice)):
                    break
                else:
                    print("Id entered is not valid")
        # assigning the type of grain name according the index of dictionary
        if choice == 1:
            name = "Rice"
        elif choice == 2:
            name = "Pulse"
        elif choice == 3:
            name = "Wheat"
        else:
            logger.error("Invalid choice")
        for j in range(len(data['inventory'][name])):  # traversing throughout the Dictionary and accessing the elements
            print(j + 1, data['inventory'][name][j]['Name'])
        choice = int(input("\nEnter your opinion: "))  # getting the grain name from the user buy
        print("Enter weight of", name, "you want purchase and add to Inventory: ")
        weight = int(input())  # getting the weight of selected grain to buy
        purchase_item(name, weight, choice)  # passing all necessary arguments to the method for further process
    except Exception as e:  # handling the exception for bad input
        logger.error(e)
        logger.info("Invalid Input")


def sell_items():
    """
    Description:
        this function is using to sell the grain from the Inventory which will reflect the amount purchased in the JSON file
    """
    print("\nChoose the item to sell\nPress 1 to sell Rice\nPress 2 to sell pulses\nPress 3 to sell "
          "wheat\n")  # displaying sub-menu
    try:
         while True:
                choice = int(input("Enter your opinion: "))
                if(re.match(re.compile(RegexPattern.NUMBER_PATTERN), choice)):
                    break
                else:
                    print("Id entered is not valid")
        # assigning the type of grain name according the index of dictionary
                if choice == 1:
                    name = "Rice"
                elif choice == 2:
                    name = "Pulse"
                elif choice == 3:
                    name = "Wheat"
                else:
                    logger.error("Invalid choice")
    except Exception as e:  # handling the exception for bad input
        logger.error(e)
        logger.info("Invalid Input")

    for j in range(len(data['inventory'][name])):  # traversing throughout the Dictionary and accessing the elements
        print(j + 1, data['inventory'][name][j]['Name'])
    choice = int(input("\nEnter your opinion: "))  # getting the grain name from the user buy
    print("Enter weight of", name, "you want sell from Inventory: ")
    weight = int(input())  # getting the weight of selected grain to buy
    sell_item(name, weight, choice)  # passing all necessary arguments to the method for further process


def add_new_item():
    """
    Description:
            displaying sub-menu
    """
    print("\nChoose the item to add\nPress 1 to add Rice\nPress 2 to add pulses\nPress 3 to add wheat\n")
    try:
         while True:
                choice = int(input("Enter your opinion: "))
                if(re.match(re.compile(RegexPattern.NUMBER_PATTERN), choice)):
                    break
                else:
                    print("Id entered is not valid")
        # assigning the type of grain name according the index of dictionary
                if choice == 1:
                    name = "Rice"
                    inventory_detail(name)  # passing the grain name to the 'inventory_detail' method to get details of
                    # selected grain to write on JSON file
                elif choice == 2:
                    name = "Pulse"
                    inventory_detail(name)  
                elif choice == 3:
                    name = "Wheat"
                    inventory_detail(name)  
                else:
                    logger.error("\nInvalid choice")
    except Exception as e:  
        logger.error(e)
        logger.info("Invalid Input")

class DataManagement:
    while True:
        print("\n                MENU\n"
              "-----------------------------------------\n"
              "1. Press 1 to display Inventory\n"
              "2. Press 2 to purchase item and add to the Inventory\n"
              "3. Press 3 to sell item from Inventory\n"
              "4. Press 4 to add new item in Inventory\n"
              "5. Press 5 to Exit \n")
        global option  
        try:
            while True:
                option = int(input("Enter your opinion: "))
                if(re.match(re.compile(RegexPattern.NUMBER_PATTERN), option)):
                    break
                else:
                    logger.error("Id entered is not valid")
        except Exception as e:  
            logger.error(e)  

        try:
            if option == 1:
                display_inventory()  
            elif option == 2:
                buy_item()  
            elif option == 3:
                sell_items()  
            elif option == 4:
                add_new_item() 
            elif option == 5:
                print("\nClosing Inventory..... \nInventory Closed.")
                exit(0)
            else:
                logger.error("Invalid Input")
        except Exception as e: 
                logger.error(e)
                logger.info("Invalid Input")


if __name__ == '__main__':
    obj = DataManagement()  