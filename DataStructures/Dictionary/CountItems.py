"""
@Author: Swapnil Bhoyar
@Date: 2021-07-04 20:14:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-04 20:14:00
@Title : Write a Python program to check multiple keys exists in a dictionary
"""
import logging
class CountItemsLog:
    logging.basicConfig(filename="CountItemsLog.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
  
    #Creating an object
    logger=logging.getLogger()
    
    #Setting the threshold of logger to ERROR
    logger.setLevel(logging.ERROR)

class CountItems:
    def getCountItems(self):
        """
        Description:
            this function count number of items in a dictionary value that is a list.
        """
        dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
        count = sum(map(len, dict.values()))
        print(count)

if __name__=="__main__":
    countItems = CountItems()
    try:
        countItems.getCountItems()
    except Exception as e:
        CountItemsLog.logger.error(e)