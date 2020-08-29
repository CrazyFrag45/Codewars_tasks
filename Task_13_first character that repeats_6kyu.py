'''
Find the first character that repeats in a String and return that character.

first_dup('tweet') => 't'
first_dup('like') => None
This is not the same as finding the character that repeats first. In that case,
 an input of 'tweet' would yield 'e'.
'''
#First:
def first_dup(s):
    for i in range(len(s)):
        if list(s).count(s[i]) > 1:
            return s[i]



#Second:
def first_dup2(s):
    return next((x for x in s if s.count(x) > 1), None)



print(first_dup('tweet'))
print(first_dup('Ode to Joy'))
print(first_dup('ode to joy'))
print(first_dup('bar'))
print(first_dup('123123'))
print(first_dup('!@#$!@#$'))
print(first_dup('1a2b3a3c'))


print(first_dup2('tweet'))
print(first_dup2('Ode to Joy'))
print(first_dup2('ode to joy'))
print(first_dup2('bar'))
print(first_dup2('123123'))
print(first_dup2('!@#$!@#$'))
print(first_dup2('1a2b3a3c'))
