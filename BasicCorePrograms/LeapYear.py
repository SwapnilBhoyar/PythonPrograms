"""
@Author: Swapnil Bhoyar
@Date: 2021-06-27 04:47:00
@Last Modified By: Swapnil Bhoyar
@Last Modified Date: 2021-06-27 04:47:00
@Title: Check if year is leap year or not?
"""

def checkYear(year):
    """
    Description:
        This fuction return true when year is a leap year
    
    Parameter:
        year is integer value taken as user input
    """

    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
             return True
    else:
        return False
 
print("Enter a year:")
year = int(input())

if (year <= 999 or year > 9999):
    print("Enter four digit value")
else:
    if(checkYear(year)):
        print("Leap Year")
    else:
        print("Not a Leap Year")
