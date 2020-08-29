'''
In this Kata, we are going to reverse a string while maintaining the spaces (if any) in their original place.

For example:

solve("our code") = "edo cruo"
-- Normal reversal without spaces is "edocruo".
-- However, there is a space after the first three characters, hence "edo cruo"

solve("your code rocks") = "skco redo cruoy"
solve("codewars") = "srawedoc"
More examples in the test cases. All input will be lower case letters and in some cases spaces.

Good luck!
'''

#First
def solve1(s):
    d = list(s)
    count_jump = 0
    for index in range(0, len(s)):
        if d[index] == ' ':
            continue
        elif index == len(s) - 1:
            count_jump = 0
            d[index] = ''.join(reversed(s))[index]
        elif ''.join(reversed(s))[index] == ' ':
            # count_jump += 1
            d[index] = ''.join(reversed(s))[index - 1]
            print(count_jump)
        else:
            d[index] = ''.join(reversed(s))[index]
            print(count_jump)
    return ''.join(d)



#Second
def solve2(s):
    return d




print(solve1("codewars")) # "srawedoc"
print(solve1("your code")) # "edoc ruoy"
print(solve1("11 22 3")) # "32 21 1"
print(solve1("your code rocks")) # "skco redo cruoy"
print(solve1("i love codewars")) # "s rawe docevoli"

