"""
@Author: Swapnil Bhoyar
@Date: 2021-06-27 03:02:00
@Last Modified By: Swapnil Bhoyar
@Last Modified Date: 2021-06-27 03:02:00
@Title: Flip Coin and print percentage of Heads and Tails
”"""
import random

print("Enter the number of times to flip the coin:")
num = int(input())
head = 0
tail = 0 

for number in range(0, num) :
    # random generate a random value between 0.0 and 0.1
    randomValue = random.random();
    if randomValue < 0.5 :
        tail += 1
    else :
        head += 1

tailPercentage = tail * 100 / num
headPercentage = head * 100 / num

print("Tail percentage is", tailPercentage,"%")
print("Head Percentage is", headPercentage,"%")