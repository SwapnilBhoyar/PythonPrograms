"""
@Author: Swapnil Bhoyar
@Date: 2021-07-06 08:52:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-05 08:52:00
@Title : Write a Python program to generate all permutations of a list in Python.
"""
from Log import Log
from itertools import permutations
class Permutation:
    """
    Description:
        this function create permutation
    """
    def getPermutation(self):
        resultList =    list(permutations(range(1, 3)))
        Log.logger.info(resultList)
       
if __name__=="__main__":
    permutation = Permutation()
    try:
        permutation.getPermutation()
    except Exception as e:
        Log.logger.error(e)
