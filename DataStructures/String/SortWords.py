"""
@Author: Swapnil Bhoyar
@Date: 2021-07-06 23:37:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-05 23:37:00
@Title : Write a Python program that accepts a comma separated sequence of words as input
and prints the unique words in sorted form (alphanumerically)
"""

from Log import Log

def sortWords():
    """
    Description:
        this function sort the comma separated value
    """
    items = 'orange,mango,banana,apple'
    words = [word for word in items.split(",")]
    print(",".join(sorted(list(set(words)))))

sortWords()