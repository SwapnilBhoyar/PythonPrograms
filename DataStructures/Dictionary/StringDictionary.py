from collections import defaultdict, Counter
"""
@Author: Swapnil Bhoyar
@Date: 2021-07-04 18:12:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-04 18:12:00
@Title : Write a Python program to create a dictionary from a string.
"""
import logging
from collections import defaultdict, Counter
class StringDictionaryLog:
    logging.basicConfig(filename="StringDictionaryLog.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
  
    #Creating an object
    logger=logging.getLogger()
    
    #Setting the threshold of logger to ERROR
    logger.setLevel(logging.ERROR)

class StringDictionary:
    def getStringDictionary(self):
        inputString = 'swapnil' 
        stringDict = {}
        for letter in inputString:
            stringDict[letter] = stringDict.get(letter, 0) + 1
        print(stringDict)

if __name__=="__main__":
    StringDictionary = StringDictionary()
    try:
        StringDictionary.getStringDictionary()
    except Exception as e:
        StringDictionaryLog.logger.error(e)
