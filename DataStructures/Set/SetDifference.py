"""
@Author: Swapnil Bhoyar
@Date: 2021-07-04 02:11:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-04 02:11:00
@Title : Write a Python program to create set difference.
"""
import logging

class SetDifferenceLog:
    logging.basicConfig(filename="SetDifferenceLog.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
  
    #Creating an object
    logger=logging.getLogger()
    
    #Setting the threshold of logger to ERROR
    logger.setLevel(logging.ERROR)

class SetDifference:
    def getSetDifference(self):
        setc1 = set(["green", "blue"])
        setc2 = set(["blue", "yellow"])

        print("Original sets:")
        print(setc1)
        print(setc2)

        r1 = setc1.difference(setc2)
        print("\nDifference of setc1 - setc2:")
        print(r1)

        r2 = setc2.difference(setc1)
        print("\nDifference of setc2 - setc1:")
        print(r2)

        setn1 = set([1, 1, 2, 3, 4, 5])
        setn2 = set([1, 5, 6, 7, 8, 9])

        print("\nOriginal sets:")
        print(setn1)
        print(setn2)

        r1 = setn1.difference(setn2)
        print("\nDifference of setn1 - setn2:")
        print(r1)

        r2 = setn2.difference(setn1)
        print("\nDifference of setn2 - setn1:")
        print(r2)

if __name__=="__main__":
    setDifference = SetDifference()
    try:
        setDifference.getSetDifference()
    except Exception as e:
        SetDifferenceLog.logger.error(e)