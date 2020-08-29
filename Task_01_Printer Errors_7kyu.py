'''
In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which, for the
sake of simplicity, are named with letters from a to m.

The colors used by the printer are recorded in a control string. For example a "good" control string would be
aaabbbbhaijjjm meaning that the printer used three times color a, four times color b, one time color h then one time
color a...

Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced e.g.
'aaaxbbbbyyhwawiwjjjwwm'.

You have to write a function printer_error which given a string will output the error rate of the printer as a string
representing a rational whose numerator is the number of errors and the denominator the length of the control string.
Don't reduce this fraction to a simpler expression.

The string has a length greater or equal to one and contains only letters from ato z.

#Examples:

s="aaabbbbhaijjjm"
error_printer(s) => "0/14"

s="aaaxbbbbyyhwawiwjjjwwm"
error_printer(s) => "8/22"
'''


# First:
def printer_error(s):
    if s.isalpha():
        s = s.lower()
        color = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
        #error = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        color_true = 0
        color_error = 0
        for i in range(0,len(s)):
            if s[i] in color:
                color_true += 1
            else:
                color_error += 1
        printer_str = str(str(color_error) + "/" + str(len(s)))

        return printer_str
    else:
        return False


#Second:
from re import sub
def printer_error1(s):
    return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))

s = 'vcjweqaaaaasssss'
print(printer_error(s))
print(printer_error1(s))

s = 'vcedSADFfyhfjnhnkhjweqCXVZXTRaaxxxsssss'
print(printer_error(s))
print(printer_error1(s))