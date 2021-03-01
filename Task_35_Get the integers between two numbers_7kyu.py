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


print(function(2, 6))  # [3,4,5,6,7,8]
print(function([2, 2, 2, 2]))  # 0
print(function([1, 1, 1, 3]))  # 2

print(function([1, 1, 3, 3]))  # 4
print(function([1, 3, 3, 3]))  # 6
print(function([3, 3, 3, 3]))  # 8
