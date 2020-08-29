'''
Simple enough this one - you will be given an array. The values in the array
will either be numbers or strings, or a mix of both. You will not get an empty
array, nor a sparse one.

Your job is to return a single array that has first the numbers sorted in
ascending order, followed by the strings sorted in alphabetic order. The values
must maintain their original type.

Note that numbers written as strings are strings and must be sorted with the
other strings.
'''
#First:
def db_sort(arr):
    digite_arr = []
    char_arr = []
    for i in range(len(arr)):
        if type(arr[i]) == int:
            digite_arr.append(arr[i])
        else:
            char_arr.append(arr[i])
    digite_arr = sorted(digite_arr)
    char_arr = sorted(char_arr)
    arr = digite_arr + char_arr
    return arr

#Second:
def db_sort2(arr):
    return sorted(arr, key=lambda x: (isinstance(x,str),x))



print(db_sort([6, 2, 3, 4, 5]))
print(db_sort([14, 32, 3, 5, 5]))
print(db_sort([1, 2, 3, 4, 5]))
print(db_sort(["Banana", "Orange", "Apple", "Mango", 0, 2, 2]))
print(db_sort(["C", "W", "W", "W", 1, 2, 0]))
print(db_sort(['come', 'on', 110, '2500', 10, '!', 7, 15, 5, 6, 6]))

print(db_sort2( [6, 2, 3, 4, 5] ))
print(db_sort2( [14, 32, 3, 5, 5] ))
print(db_sort2( [1, 2, 3, 4, 5] ))
print(db_sort2( ["Banana", "Orange", "Apple", "Mango", 0, 2, 2] ))
print(db_sort2( ["C", "W", "W", "W", 1, 2, 0]))
print(db_sort2( ['come', 'on', 110, '2500', 10, '!', 7, 15, 5, 6, 6] ))
