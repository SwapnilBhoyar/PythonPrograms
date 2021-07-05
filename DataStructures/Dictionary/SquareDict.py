"""
@Author: Swapnil Bhoyar
@Date: 2021-07-04 16:18:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-04 16:18:00
@Title : Write a Python script to generate and print a dictionary that contains a
number (between 1 and n) in the form (x, x*x).
"""
from Log import Log

class SquareDict:
    def getSquareDict(self):

        number=int(input("Input a number "))
        dictionary = dict()

        for x in range(1,number+1):
            dictionary[x]=x*x

        print(dictionary) 

squareDict = SquareDict()
try:
    squareDict.getSquareDict()
except Exception as e:
    Log.logger.error(e)   