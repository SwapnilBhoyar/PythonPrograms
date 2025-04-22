# The task is to find all unique pairs of numbers in the array arr that add up to a given target value.

# Key Details:
# Input:
# An array arr of integers: [1, 2, 3, 4, 5, 6, 7, 8, 9].
# A target sum: 10.

arr = [1,2,3,4,5,6,7,8,9]

target = 10
res_list = []
occured = []
for i in range(len(arr)):
    ele = target - arr[i]
    if ele in arr and arr[i] not in occured and arr[i] != ele:
        res_list.append((arr[i],ele))
        occured.append(ele)
print(res_list)

# answer = [(1, 9), (2, 8), (3, 7), (4, 6)]