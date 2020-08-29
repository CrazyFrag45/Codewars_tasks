'''The goal of this exercise is to convert a string to a new string where each character in the new string is '('
if that character appears only once in the original string, or ')' if that character appears more than once in the
original string. Ignore capitalization when determining if a character is a duplicate.

Examples:

"din" => "((("

"recede" => "()()()"

"Success" => ")())())"

"(( @" => "))(("

Notes:

Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX",
the "XXX" is actually the expected result, not the input! (these languages are locked so that's not possible to
correct it).
'''

#First var:
def duplicate_encode(word):
    word = word.lower()
    word_res = ''
    for i in range(0, len(word)):
        if word.count(word[i]) == 1:
            word_res += '('
        else:
            word_res += ')'
    return word_res

#Second var:
def duplicate_encode2(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

word = 'Papper'

print(duplicate_encode(word))
print(duplicate_encode2(word))
