"""
@Author: Swapnil Bhoyar
@Date: 2021-07-04 16:18:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-04 16:18:00
@Title : Write a Python script to generate and print a dictionary that contains a
number (between 1 and n) in the form (x, x*x).
"""
import logging

class SquareDictLog:
    logging.basicConfig(filename="SquareDictLog.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
  
    #Creating an object
    logger=logging.getLogger()
    
    #Setting the threshold of logger to ERROR
    logger.setLevel(logging.ERROR)

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
    SquareDictLog.logger.error(e)   