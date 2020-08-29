'''
In this Kata, you will be given a string and your task will be to return the length of the longest prefix
that is also a suffix. A prefix is the start of a string while the suffix is the end of a string.
For instance, the prefixes of the string "abcd" are ["a","ab","abc"]. The suffixes are ["bcd", "cd", "d"].
You should not overlap the prefix and suffix.
'''

#First
def solve(st):
    for i in range(len(st) // 2, 0, -1):
        if st[:i] == st[-i:]:
            return i
    return 0
#Second
def solve2(st):
    return next((n for n in range(len(st)//2, 0, -1) if st[:n] == st[-n:]), 0)



print('result = ', solve("abcd")) #0
print('result = ', solve("abcda")) #1
print('result = ', solve("abcdabc")) #3
print('result = ', solve("abcabc")) #3
print('result = ', solve("abcabca")) #1
print('result = ', solve("aaaaa")) #2
print('result = ', solve("aaaa")) #2
print('result = ', solve("aaa")) #1
print('result = ', solve("aa")) #1
print('result = ', solve("a")) #0