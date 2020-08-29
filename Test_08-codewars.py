'''
Write a function called that takes a string of parentheses, and determines
if the order of the parentheses is valid. The function should return true if
the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true

Constraints
0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any
valid ASCII characters. Furthermore, the input string may be empty and/or
not contain any parentheses at all. Do not treat other forms of brackets as
parentheses (e.g. [], {}, <>).
'''
def valid_parentheses(string):
    if string.count('(') != string.count(')'):
        return False
    elif string.find('(') > string.find(')'):
        return False
    elif string.rfind('(') > string.rfind(')'):
        return False
    sum_1, sum_2 = 0, 0
    for i in range(len(string)-1):
        if sum_2 > sum_1:
            return False
        elif string[i] == '(':
            sum_1 += 1
        elif string[i] == ')':
            sum_2 += 1
    return True


print(valid_parentheses("  ("))  #False
print(valid_parentheses(")test"))  #False
print(valid_parentheses(""))  #True
print(valid_parentheses("hi())("))  #False
print(valid_parentheses("hi(hi)()"))  #True

def valid_parentheses2(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False

print(valid_parentheses2("  ("))  #False
print(valid_parentheses2(")test"))  #False
print(valid_parentheses2(""))  #True
print(valid_parentheses2("hi())("))  #False
print(valid_parentheses2("hi(hi)()"))  #True
