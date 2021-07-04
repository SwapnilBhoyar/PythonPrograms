"""
@Author: Swapnil Bhoyar
@Date: 2021-07-04 02:24:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-04 02:24:00
@Title : Write a Python program to create a symmetric difference..
"""
import logging

class SymmetricDifferenceLog:
    logging.basicConfig(filename="SymmetricDifferenceLog.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
  
    #Creating an object
    logger=logging.getLogger()
    
    #Setting the threshold of logger to ERROR
    logger.setLevel(logging.ERROR)

class SymmetricDifference:
    def getSymmetric(self):
        """
        Description:
            this function perform symmetric difference
        """
        setc1 = set(["green", "blue"])
        setc2 = set(["blue", "yellow"])

        print("Original sets:")
        print(setc1)
        print(setc2)

        r1 = setc1.symmetric_difference(setc2)
        print("\nSymmetric difference of setc1 - setc2:")
        print(r1)

        r2 = setc2.symmetric_difference(setc1)
        print("\nSymmetric difference of setc2 - setc1:")
        print(r2)

        setn1 = set([1, 1, 2, 3, 4, 5])
        setn2 = set([1, 5, 6, 7, 8, 9])

        print("\nOriginal sets:")
        print(setn1)
        print(setn2)

        r1 = setn1.symmetric_difference(setn2)
        print("\nSymmetric difference of setn1 - setn2:")
        print(r1)

        r2 = setn2.symmetric_difference(setn1)
        print("\nSymmetric difference of setn2 - setn1:")
        print(r2)

if __name__=="__main__":
    symmetricDifference = SymmetricDifference()
    try:
        symmetricDifference.getSymmetric()
    except Exception as e:
        SymmetricDifferenceLog.logger.error(e)