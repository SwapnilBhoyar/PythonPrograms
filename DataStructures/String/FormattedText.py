"""
@Author: Swapnil Bhoyar
@Date: 2021-07-07 9:48:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-07 09:48:00
@Title : Write a Python program to display formatted text (width=50) as output.
"""

from Log import Log
import textwrap

def formattedText():
    sampleText = '''
    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
    '''

    Log.logger.info(textwrap.fill(sampleText, width=50))

formattedText()
