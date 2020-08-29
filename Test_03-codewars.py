'''In this little assignment you are given a string of space separated numbers, and have to return the highest
and lowest number.

Example:

high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"'''

#First var:
def high_and_low(numbers):
    numbers = numbers.split(' ')
    numbers_2 = [int(i) for i in numbers]
    res = str(max(list(numbers_2))) + ' ' + str(min(list(numbers_2)))
    return res

#Second var:
def high_and_low2(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))


numbers = ('4 5 29 54 4 0 -214 542 -64 1 -3 6 -6')


print(high_and_low(numbers))
print(high_and_low2(numbers))
