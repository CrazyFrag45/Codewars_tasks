'''
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer
'''


# First:
def square_digits(num):
    if num > 0:
        res = ''
        while num > 0:
            d = (num % 10) ** 2
            num = num // 10
            res = str(d) + str(res)
        return int(''.join(res))
    else:
        pass


print(square_digits(9119))
print(square_digits(16572))
print(square_digits(3623))
