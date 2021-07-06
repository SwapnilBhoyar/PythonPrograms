"""
@Author: Swapnil Bhoyar
@Date: 2021-07-06 23:37:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-05 23:37:00
@Title : Write a Python script that takes input from the user and displays that input back in
upper and lower cases."""

from Log import Log

def upperLowerCase():
    """
    Description:
        this program gives upper and lower case
    """
    stringName = "Swapnil"

    Log.logger.info(stringName.upper())
    Log.logger.info(stringName.lower())

upperLowerCase()
