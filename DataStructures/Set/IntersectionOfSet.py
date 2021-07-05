"""
@Author: Swapnil Bhoyar
@Date: 2021-07-04 01:36:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-04 01:36:00
@Title : Write a Python program to create an intersection of sets.
"""
from Log import Log

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
        Log.logger.error(e)