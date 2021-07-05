"""
@Author: Swapnil Bhoyar
@Date: 2021-07-05 10:10:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-05 10:10:00
@Title : Write a Python program to use of frozensets.
"""
import logging

class FrozenSetLog:
    logging.basicConfig(filename="FrozenSetLog.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
  
    #Creating an object
    logger=logging.getLogger()
    
    #Setting the threshold of logger to ERROR
    logger.setLevel(logging.ERROR)

class FrozenSet:
    """
    Description:
        this function consist frozenset
    """
    def getFrozenSet(self):
        #frozenset in immutable cant change values
        x = frozenset([1, 2, 3, 4, 5])
        y = frozenset([3, 4, 5, 6, 7])

        #use isdisjoint() function of frozenset. Return True if the set has no elements in common with other. 
        print(x.isdisjoint(y))

        #use difference() function of frozenset. Return a new set with elements in the set that are not in the others.
        print(x.difference(y))

        #new set with elements from both x and y
        print(x | y)

if __name__=="__main__":
    frozenSet = FrozenSet()
    try:
        frozenSet.getFrozenSet()
    except Exception as e:
        FrozenSetLog.logger.error(e)    