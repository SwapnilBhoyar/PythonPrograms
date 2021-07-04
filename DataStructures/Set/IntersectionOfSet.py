"""
@Author: Swapnil Bhoyar
@Date: 2021-07-04 01:36:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-04 01:36:00
@Title : Write a Python program to create an intersection of sets.
"""
import logging

class IntersectionOfSetsLog:
    logging.basicConfig(filename="IntersectionOfSetsLog.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
  
    #Creating an object
    logger=logging.getLogger()
    
    #Setting the threshold of logger to ERROR
    logger.setLevel(logging.ERROR)

class IntersectionOfSets:
    def getIntersection(self):
        """
        Description:
            this function intersect sets
        """
        setx = set(["green", "blue"])
        sety = set(["blue", "yellow"])
        print("Original set elements:")
        print(setx)
        print(sety)
        print("\nIntersection of two said sets:")
        setz = setx & sety
        print(setz)

if __name__=="__main__":
    intersectionOfSets = IntersectionOfSets
    try:
        intersectionOfSets.getIntersection()
    except Exception as e:
        IntersectionOfSetsLog.logger.error(e)