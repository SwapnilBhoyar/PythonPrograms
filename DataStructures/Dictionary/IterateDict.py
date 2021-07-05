"""
@Author: Swapnil Bhoyar
@Date: 2021-07-04 16:18:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-04 16:18:00
@Title : this program iterate dictionary.
"""
from Log import Log

class IterateDict:
    """
    Description:
        this function iterate dictionary
    """
    def iterate(self):
        dctionary = {'Red': 1, 'Green': 2, 'Blue': 3}

        for colorKey, value in dctionary.items():
            print(colorKey, ':', dctionary[colorKey]) 

if __name__=="__main__":
    iterateDict = IterateDict()
    try:
        iterateDict.iterate()
    except Exception as e:
        Log.logger(e)

