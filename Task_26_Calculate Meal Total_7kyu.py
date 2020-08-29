'''
Create a function that returns the total of a meal including tip and tax. You should not tip on the tax.

You will be given the subtotal, the tax as a percentage and the tip as a percentage. Please round your result to two
decimal places.
'''


# First:
def calculate_total(subtotal, tax, tip):
    return round(subtotal + subtotal * (tax / 100) + subtotal * (tip / 100), 2)


print(calculate_total(120, 10, 5))
print(calculate_total(3220, 23, 17))
