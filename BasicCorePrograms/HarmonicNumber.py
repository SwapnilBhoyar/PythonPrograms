"""
@Author: Swapnil Bhoyar
@Date: 2021-06-27 18:04:00
@Last Modified By: Swapnil Bhoyar
@Last Modified Date: 2021-06-27 18:04:00
@Title: This program takes a command-line argument N and prints a table of the
powers of 2 that are less than or equal to 2^N.
"""

def nthHarmonic(number) :
    """
    Description:
        This function genrate harmonic number of nth number
    
    Parameter:
        number parameter is nth harmonic value
        
    Return:
        harmonic return value is nth harmonic value"""
 
    harmonic = 1.00

    for i in range(2, number + 1) :
        harmonic += 1 / i
 
    return harmonic

print("Enter a number:")
number = int(input())
print(round(nthHarmonic(number),2))