'''
Write a function that takes an array of numbers (integers for the tests) and a
target number. It should find two different items in the array that, when added
together, give the target value. The indices of these items should then be
returned in an array like so: [index1, index2].

For the purposes of this kata, some tests may have multiple answers; any valid
solutions will be accepted.

The input will always be valid (numbers will be an array of length 2 or greater,
 and all of the items will be numbers; target will always be the sum of two
 different items from that array).

Based on: http://oj.leetcode.com/problems/two-sum/
'''
#First:
def two_sum(numbers, target):
    j = 0
    for i in range(len(numbers)):
        if i != j and target == numbers[i] + numbers[j]:
            return [i, j]
        else:
            for j in range(len(numbers)):
                if i != j and target == numbers[i] + numbers[j]:
                    return [i, j]



#Second:
def two_sum2(numbers, target):
    for i, x in enumerate(numbers):
        for j, y in enumerate(numbers):
            if i != j and x + y == target:
                return [i, j]



print(two_sum([1,2,3], 4))
print(two_sum([1234,5678,9012], 14690))
print(two_sum([2,2,3], 4))


print(two_sum2([1,2,3], 4))
print(two_sum2([1234,5678,9012], 14690))
print(two_sum2([2,2,3], 4))
