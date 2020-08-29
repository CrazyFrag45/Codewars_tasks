'''
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.

'''

#First:
def make_readable(seconds):
    if seconds <= 59:
        return '00:00:{sec:{c}>{n}}'.format(sec = seconds, n = 2, c = "0")
    elif seconds <= 3599:
        return '00:{min:{c}>{n}}:{sec:{c}>{n}}'.format(min = seconds//60,
                sec = seconds - ((seconds//60) * 60), n = 2, c = "0")
    else:
        return '{hou:{c}>{n}}:{min:{c}>{n}}:{sec:{c}>{n}}'.format(hou = seconds//3600,
                min = (seconds - ((seconds//3600) * 3600))//60,
                sec = seconds - (((seconds//3600) * 3600) +
                ((seconds - ((seconds//3600) * 3600))//60) * 60), n = 2, c = "0")




#Second:
def make_readable2(seconds):
    return "%02d:%02d:%02d" % (seconds//3600, seconds % 3600 / 60, seconds % 3600 % 60)



print(make_readable(0))
print(make_readable(5))
print(make_readable(60))
print(make_readable(86399))
print(make_readable(359999))


print()
print('   and   ')


print(make_readable2(0))
print(make_readable2(5))
print(make_readable2(60))
print(make_readable2(86399))
print(make_readable2(359999))
