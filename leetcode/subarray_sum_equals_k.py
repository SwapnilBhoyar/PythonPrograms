nums = [3, 4, 7, 2, -3, 1, 4, 2, 1]


count = 0
curr_sum = 0
k = 7
sum_dict = {0:1}
for num in nums:
    curr_sum += num
    diff = curr_sum - k
    if diff in sum_dict:
        count = count + sum_dict[diff]
    if curr_sum in sum_dict:
        sum_dict[curr_sum] += 1
    else:
        sum_dict[curr_sum] =1


# sum_dict:{0: 1, 3: 1, 7: 1, 14: 2, 16: 1, 13: 1, 18: 1, 20: 1, 21: 1}
# count:6