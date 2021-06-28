"""
@Author: Swapnil Bhoyar
@Date: 2021-06-28 21:05:00
@Last Modified By: Swapnil Bhoyar
@Last Modified Date: 2021-06-28 21:05:00
@Title: Find roots of equation 
"""
import math

def findRoots( a, b, c): 
    """
    Description:
        this function find roots for quadraitc equation
    Parameter:
        a parameter consist fist value
        b parameter consist second value
        c parameter consist third value
    """
    delta = b * b - 4 * a * c 
    sqrt_val = math.sqrt(abs(delta)) 
      
    if delta > 0: 
        print(" real and different roots ") 
        print((-b + sqrt_val)/(2 * a)) 
        print((-b - sqrt_val)/(2 * a)) 
      
    elif delta == 0: 
        print(" real and same roots") 
        print(-b / (2 * a)) 
      
    # when delta is less than 0
    else:
        print("Complex Roots") 
        print(- b / (2 * a), " + i", sqrt_val) 
        print(- b / (2 * a), " - i", sqrt_val) 
   
try:
    a = int(input("Enter a non zero value:"))
    b = int(input("Enter a value:"))
    c = int(input("Enter a value:"))
except:
    print("Enter proper value") 

# If a is 0, then incorrect equation
if a == 0: 
        print("Input correct quadratic equation") 
  
else:
    findRoots(a, b, c)