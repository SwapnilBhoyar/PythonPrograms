"""
@Author: Swapnil Bhoyar
@Date: 2021-07-04 15:19:00
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 15:19:00
@Title : this program concatinate dictionary.
"""
import logging

class ConcatinateLog:
    logging.basicConfig(filename="ConcatinateLog.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
  
    #Creating an object
    logger=logging.getLogger()
    
    #Setting the threshold of logger to ERROR
    logger.setLevel(logging.ERROR)
class Concatinate:
    """
    Description:
        this function concatinate dictionary
    """
    def getConcatinate(self):
        firstDict={1:10, 2:20}
        secondDict={3:30, 4:40}
        thirdDict={5:50,6:60}
        fourthDict = {}
        for dictionary in (firstDict, secondDict, thirdDict): fourthDict.update(dictionary)
        print(fourthDict)

if __name__=="__main__":
    Concatinate = Concatinate()
    try:
        Concatinate.getConcatinate()
    except Exception as e:
        ConcatinateLog.logger.error(e)