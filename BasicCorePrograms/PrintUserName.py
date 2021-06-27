"""
@Author: Swapnil Bhoyar
@Date: 2021-06-27 12:00:00
@Last Modified By: Swapnil Bhoyar
@Last Modified Date: 2021-06-27 12:00:00
@Title: User Input and Replace String Template “Hello <<UserName>>, How are you?
”"""

userName = input("Enter name:")
if len(userName) < 3:
    print("Enter name with minimum 3 character long")

else:
    print("Hello",userName,",How are you?")
