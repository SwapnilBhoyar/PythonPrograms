"""
@Author: Swapnil Bhoyar
@Date: 2021-06-28 19:00:00
@Last Modified By: Swapnil Bhoyar
@Last Modified Date: 2021-06-28 19:00:00
@Title: Find Euclidean distance between two integers 
"""
import math

def calculateDistance(firstPoint, secondPoint):
    """
    Description:
        this function find euclidean distance between two points
    Parameter:
        firstPoint parameter consist first point
        secondPoint parameter consist second point
    Return:
        return euclidean distance
    """
    distance = math.sqrt(firstPoint ** 2 + secondPoint ** 2)
    return distance

try:
    firstPoint = int(input("Enter first point value:"))
    secondPoint = int(input("Enter second point value:"))

    distance = calculateDistance(firstPoint, secondPoint)
except ValueError:
    print("Enter proper value") 
    
print("Distance:", distance)