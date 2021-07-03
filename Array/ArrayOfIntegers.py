from array import *
import logging

class ArrayOfIntegersLog:
    logging.basicConfig(filename="ArrayOfIntegersLog.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
  
    #Creating an object
    logger=logging.getLogger()
    
    #Setting the threshold of logger to DEBUG
    logger.setLevel(logging.DEBUG)
    
class ArrayOfIntegers:
    def getArray(self):
    
        integerArray = array('i', [10,20,30,40,50])

        print(integerArray[0])
        print(integerArray[1])
        print(integerArray[2])
        print(integerArray[3])
        print(integerArray[4])

if __name__ == "__main__":

    arrayOfIntegers = ArrayOfIntegers()
    try:
        arrayOfIntegers.getArray()
    except Exception as e:
        ArrayOfIntegersLog.logger.error(e)