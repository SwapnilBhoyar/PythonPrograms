"""
@Author: Swapnil Bhoyar
@Date: 2021-06-27 05:28:00
@Last Modified By: Swapnil Bhoyar
@Last Modified Date: 2021-06-27 05:28:00
@Title: This program takes a command-line argument N and prints a table of the
powers of 2 that are less than or equal to 2^N.
"""
import math

number = int(input("Enter number"))
if number > 31 and number >= 0:
    print("Enter number between 1 and 31")
else:
    for num in range(number):
        # pow function give power of given numbers
        power = pow(2, num)
        print(power)