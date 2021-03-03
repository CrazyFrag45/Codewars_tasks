'''
Build a function that can get all the integers between two given numbers.

Example:

(2,9)

Should give you this output back:

[ 3, 4, 5, 6, 7, 8 ]

If start_num is the same as end_num, return an empty sequence.

'''


# First:
def function(start_num, end_num):
    nums = []
    nums.extend(i for i in range(start_num, end_num) if i < end_num and i > start_num)
    return nums


# Second:
def function2(start_num, end_num):
    return list(range(start_num + 1, end_num))


print(function(2, 9))  # [3,4,5,6,7,8]
print(function(6, 8))  # [7]
print(function(2, 9))  # [3,4,5,6,7,8]
print(function(3, 5))  # [4]
print(function(5, 9))  # [6, 7, 8]
print(function(2, 5))  # [3, 4,]

print(function2(2, 9))  # [3,4,5,6,7,8]
print(function2(6, 8))  # [7]
print(function2(2, 9))  # [3,4,5,6,7,8]
print(function2(3, 5))  # [4]
print(function2(5, 9))  # [6, 7, 8]
print(function2(2, 5))  # [3, 4,]
