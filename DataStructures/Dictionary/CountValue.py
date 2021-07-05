"""
@Author: Swapnil Bhoyar
@Date: 2021-07-04 19:46:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-04 19:46:00
@Title : Write a Python program to count the values associated with key in a
dictionary.
"""
from Log import Log

class CountValue:
    def getCountValue(self):
        """
        Description:
            this funntion count value associated with key
        """
        student = [{'id': 1, 'success': True, 'name': 'Lary'},
        {'id': 2, 'success': False, 'name': 'Rabi'},
        {'id': 3, 'success': True, 'name': 'Alex'}]

        print(sum(d['id'] for d in student))
        print(sum(d['success'] for d in student))

if __name__=="__main__":
    countValue = CountValue()
    try:
        countValue.getCountValue()
    except Exception as e:
        Log.logger.error(e)