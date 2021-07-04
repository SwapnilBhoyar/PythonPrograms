"""
@Author: Swapnil Bhoyar
@Date: 2021-07-04 20:14:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-04 20:14:00
@Title : Write a Python program to check multiple keys exists in a dictionary
"""
import logging
class MultipleKeysLog:
    logging.basicConfig(filename="MultipleKeysLog.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
  
    #Creating an object
    logger=logging.getLogger()
    
    #Setting the threshold of logger to ERROR
    logger.setLevel(logging.ERROR)

class MultipleKeys:
    def checkMultipleKeys(self):
        """
        Description:
            this function check multiple keys exists in a dictionary
        """
        student = {
        'name': 'Alex',
        'class': 'V',
        'roll_id': '2'
        }
        print(student.keys() >= {'class', 'name'})
        print(student.keys() >= {'name', 'Alex'})
        print(student.keys() >= {'roll_id', 'name'})

if __name__=="__main__":
    multipleKeys = MultipleKeys()
    try:
        multipleKeys.checkMultipleKeys()
    except Exception as e:
        MultipleKeysLog.logger.error(e)