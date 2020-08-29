'''
Define a function that takes in two numbers a and b and returns the last decimal
 digit of a^b. Note that a and b may be very large!

For example, the last decimal digit of 9^7 is 9, since 9^7 = 4782969. The last
decimal digit of (2^200)^(2^300), which has over 10^92 decimal digits, is 6.

The inputs to your function will always be non-negative integers.

Examples
last_digit(4, 1)                # returns 4
last_digit(4, 2)                # returns 6
last_digit(9, 7)                # returns 9
last_digit(10, 10 ** 10)        # returns 0
last_digit(2 ** 200, 2 ** 300)  # returns 6

Remarks
JavaScript, C++, R
Since these languages don't have native arbitrarily large integers, your
arguments are going to be strings representing non-negative integers.
'''
#First:
def last_digit(n1, n2):
    if n2 == 0:
        res = 1
    elif n2 < 10:
        res = int(str(n1)[-1]) ** n2
    elif str(n1)[-1] == '0' and str(n2)[-1] == '0':
        res = 0
    else:
        res = int(str(n1)[-1]) ** (int(str(n2)[-2] + str(n2)[-1]))
    return int(str(res)[-1])



#Second:
def last_digit2(n1, n2):
    return (n1 % 10) ** (n2 % 4 + 4 * bool(n2)) % 10


print(last_digit(4, 1))
print(last_digit(4, 2))
print(last_digit(9, 7))
print(last_digit(10, 10 ** 10))
print(last_digit(2 ** 200, 2 ** 300))
print(last_digit(
    3715290469715693021198967285016729344580685479654510946723,
    68819615221552997273737174557165657483427362207517952651)
      )
print()
print('   and   ')


print(last_digit2(4, 1))
print(last_digit2(4, 2))
print(last_digit2(9, 7))
print(last_digit2(10, 10 ** 10))
print(last_digit2(2 ** 200, 2 ** 300))
print(last_digit2(
    3715290469715693021198967285016729344580685479654510946723,
    68819615221552997273737174557165657483427362207517952651)
      )
