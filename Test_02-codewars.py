'''Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 integers.
No floats or empty arrays will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455.'''

def sum_two_smallest_numbers(numbers):
    numbers = sorted(numbers)
    return numbers[0] + numbers[1]


def sum_two_smallest_numbers1(numbers):
    return sum(sorted(numbers)[:2])

numbers = [346346, 12, 10, 36, 564856, 2313425]
print(sum_two_smallest_numbers(numbers))
print(sum_two_smallest_numbers1(numbers))
