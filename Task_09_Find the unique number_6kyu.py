'''
There is an array with some numbers. All numbers are equal except for one. Try to find it!

findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55
It’s guaranteed that array contains more than 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:

Find the unique number (this kata)
Find the unique string
Find The Unique
'''


#First:
def find_uniq(arr):
    a_set = list(set(arr))
    b_arr = arr[0:3]
    if b_arr.count(a_set[0]) > b_arr.count(a_set[1]):
        return a_set[1]
    else:
        return a_set[0]
#Second:
def find_uniq2(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b

print(find_uniq( [1, 1, 1, 2, 1, 1] ))
print(find_uniq( [0, 0, 0.55, 0, 0] ))
print(find_uniq( [3, 10, 3, 3, 3] ))

print(find_uniq2( [1, 1, 1, 2, 1, 1] ))
print(find_uniq2( [0, 0, 0.55, 0, 0] ))
print(find_uniq2( [3, 10, 3, 3, 3] ))
