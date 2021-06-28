"""
@Author: Swapnil Bhoyar
@Date: 2021-06-28 19:00:00
@Last Modified By: Swapnil Bhoyar
@Last Modified Date: 2021-06-29 00:50:00
@Title: Read in N integers and counts the
number of triples that sum to exactly 0.
"""
def findTriplets(elementList, numberOfElements):
    """
    Description:
        this function finds triplet with sum 0
    Parameter:
        elementList consist this elements for triplets
        numberOfElements represents size of elementList 
    """
    FOUND = False
    for i in range(0, numberOfElements-2):
     
        for j in range(i+1, numberOfElements-1):
         
            for k in range(j+1, numberOfElements):
             
                if (elementList[i] + elementList[j] + elementList[k] == 0):
                    print(elementList[i], elementList[j], elementList[k])
                    FOUND = True

    if (FOUND == False):
        print("no triplet with sum zero exist")
 
elementList = []

try:
    numberOfElements = int(input("Enter size:"))
except Exception as e:
    print("Enter proper value", e)

for element in range(numberOfElements):
    elementList.append(int(input("Enter the elements:")))

findTriplets(elementList, numberOfElements)