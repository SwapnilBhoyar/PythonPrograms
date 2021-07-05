"""
@Author: Swapnil Bhoyar
@Date: 2021-07-04 01:55:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-04 01:55:00
@Title : Write a Python program to create a union of sets.
"""
from Log import Log
class UnionOfSet:
    """
    Description:
        this function perform union of sets
    """
    def getUnionOfSet(self):
        setc1 = set(["green", "blue"])
        setc2 = set(["blue", "yellow"])

        print("Original sets:")
        print(setc1)
        print(setc2)

        setc = setc1.union(setc2)
        print("\nUnion of above sets:")
        print(setc)

        setn1 = set([1, 1, 2, 3, 4, 5])
        setn2 = set([1, 5, 6, 7, 8, 9])

        print("\nOriginal sets:")
        print(setn1)
        print(setn2)

        print("\nUnion of above sets:")
        setn = setn1.union(setn2)
        print(setn)

if __name__=="__main__":
    unionOfSet = UnionOfSet()
    try:
        unionOfSet.getUnionOfSet()
    except Exception as e:
        Log.logger.error(e)