'''
The vowel substrings in the word codewarriors are o,e,a,io. The longest of these has a length of 2. Given
a lowercase string that has alphabetic characters only and no spaces, return the length of the longest vowel
substring. Vowels are any of aeiou.

Good luck!
If you like substring Katas, please try:

Non-even substrings
Vowel-consonant lexicon
'''
#First
def solve(s):
    list = ['a','e','i','o','u']
    max_1 = 0
    i = 0
    for k in s:
        if k in list:
            i += 1
        else:
            max_1 =  max(max_1, i)
            i = 0
    return max_1

#Second
def solve2(s):
    return max(map(len, ''.join(c if c in 'aeiou' else ' ' for c in s).split()))

print(solve('codewarriors'))
print(solve2('codewarriors'))