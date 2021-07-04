"""
@Author: Swapnil Bhoyar
@Date: 2021-07-04 00:41:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-04 00:41:00
@Title : Write a Python program to add member(s) in a set.
"""
import logging

class AddSetLog:
    logging.basicConfig(filename="AddSetLog.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
  
    #Creating an object
    logger=logging.getLogger()
    
    #Setting the threshold of logger to ERROR
    logger.setLevel(logging.ERROR)

class AddSet:
    def checkAddSet(self):
        """
        Description
            this function add element to set
        """
        colorSet = set()
        print(colorSet)

        print("\nAdd single element:")
        colorSet.add("Red")
        print(colorSet)

        print("\nAdd multiple items:")
        colorSet.update(["Blue", "Green"])
        print(colorSet)

if __name__=="__main__":
    addSet = AddSet()
    try:
        addSet.checkAddSet()
    except Exception as e:
        AddSetLog.logger.error(e)