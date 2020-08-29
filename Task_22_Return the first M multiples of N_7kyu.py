'''
Implement a function, multiples(m, n), which returns an array of the first m multiples of the real number n.
Assume that m is a positive integer.
Ex.
multiples(3, 5.0)

should return
[5.0, 10.0, 15.0]
'''

#First
def multiples(m, n):
    array_multiples = []
    for i in range(1, m+1):
        array_multiples.append(float(i*n))
    return array_multiples

#Second
def multiples2(m, n):
    return [i * n for i in range(1, m + 1)]




print('result = ', multiples(3, 5)) #[5, 10, 15])
print('result = ', multiples2(3, 5)) #[5, 10, 15])
