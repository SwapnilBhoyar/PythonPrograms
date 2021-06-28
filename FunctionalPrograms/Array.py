"""
@Author: Swapnil Bhoyar
@Date: 2021-06-28 15:26:00
@Last Modified By: Swapnil Bhoyar
@Last Modified Date: 2021-06-28 15:26:00
@Title: A library for reading in 2D arrays of integers, doubles, or booleans from
standard input and printing them out to standard output.
"""
def getArray(numberOfRows, numberOfColumns):
    """
    Description:
        this function generate 2d array
    Parameter:
        numberOfRows parameter is number of rows as input
        numberOfColumns parameter is number of columns as input 
    Return:
        this function returns a multi list
    """
    arrayList = [[0 for col in range(numberOfRows)] for row in range(numberOfColumns)]

    try:
        for row in range(numberOfRows):
            for col in range(numberOfColumns):
                arrayList[row][col]= int(input())
        return arrayList
    except IndexError:
        print("Enter proper input")

numberOfRows = int(input("Enter number of rows:"))
numberOfColumns = int(input("Enter number of columns:"))

arrayList = getArray(numberOfRows, numberOfColumns)
print(arrayList)