"""
@Author: Swapnil Bhoyar
@Date: 2021-07-04 16:18:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-04 16:18:00
@Title : this program iterate dictionary.
"""
import logging

class IterateLog:
    logging.basicConfig(filename="IterateLog.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
  
    #Creating an object
    logger=logging.getLogger()
    
    #Setting the threshold of logger to ERROR
    logger.setLevel(logging.ERROR)

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
        IterateLog.logger(e)

