"""
@Author: Swapnil Bhoyar
@Date: 2021-07-02 
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-03 01:21:00
@Title : This program implement inventory management system
"""
import logging
logger = logging
   
# logging basic config method and saving log files
logger.basicConfig(filename='inventoryInfo.log', level=logging.INFO,
                    format='%(asctime)s:%(funcName)s:%(levelname)s:%(message)s')
logger.basicConfig(filename='enventoryInfo.log', level=logging.ERROR,
                    format='%(asctime)s:%(funcName)s:%(levelname)s:%(lineno)d')