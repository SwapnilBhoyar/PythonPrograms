"""
@Author: Swapnil Bhoyar
@Date: 2021-07-04 18:12:00
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 18:12:00
@Title : Write a Python program to print all unique values in a dictionary..
"""
import logging

class UniqueDictionaryLog:
    logging.basicConfig(filename="UniqueDictionaryLog.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
  
    #Creating an object
    logger=logging.getLogger()
    
    #Setting the threshold of logger to ERROR
    logger.setLevel(logging.ERROR)

class UniqueDictionary:
    """
    Description:
        Write a Python program to print all unique values in a dictionary.
    """
    def getUniqueDictionary(self):
        dictionary = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
        print("Original List: ",dictionary)
        uniqueDict = set( val for dic in dictionary for val in dic.values())
        print("Unique Values: ",uniqueDict)

if __name__=="__main__":
    uniqueDictionary = UniqueDictionary()
    try:
        uniqueDictionary.getUniqueDictionary()
    except Exception as e:
        UniqueDictionaryLog.logger.error(e)