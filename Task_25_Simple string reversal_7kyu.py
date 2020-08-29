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


# First
def solve1(s):
    new_list = (list(filter(lambda a: a != ' ', s)))
    new_list.reverse()
    new_list2 = new_list.copy()
    for i in range(0, len(s)):
        if s[i] == ' ':
            new_list2.insert(i, ' ')

    return ''.join(new_list2)


# Second
def solve2(s):
    it = reversed(s.replace(' ', ''))
    return ''.join(c if c == ' ' else next(it) for c in s)


print(solve1("codewars"))  # "srawedoc"
print(solve1("your code"))  # "edoc ruoy"
print(solve1("11 22 3"))  # "32 21 1"
print(solve1("your code rocks"))  # "skco redo cruoy"
print(solve1("i love codewars"))  # "s rawe docevoli"

print(solve2("codewars"))  # "srawedoc"
print(solve2("your code"))  # "edoc ruoy"
print(solve2("11 22 3"))  # "32 21 1"
print(solve2("your code rocks"))  # "skco redo cruoy"
print(solve2("i love codewars"))  # "s rawe docevoli"
