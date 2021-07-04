"""
@Author: Swapnil Bhoyar
@Date: 2021-07-04 23:39:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-04 23:39:00
@Title : Write a Python program to create a set.
"""
import logging

class CreateSetLog:
    logging.basicConfig(filename="CreateSetLog.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
  
    #Creating an object
    logger=logging.getLogger()
    
    #Setting the threshold of logger to ERROR
    logger.setLevel(logging.ERROR)

class CreateSet:
    def getSet(self):
        """
        Description:
            this function contains set
        """
        intSet = set([0, 1, 2, 3, 4])
        print(intSet)

        mixSet = {1,2,3,'foo','bar'}
        print(mixSet)

if __name__=="__main__":
    createSet = CreateSet()
    try:
        createSet.getSet()
    except Exception as e:
            CreateSetLog.logger.error(e)