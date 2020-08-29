'''
All we eat is water and dry matter.
John bought potatoes: their weight is 100 kilograms. Potatoes contain water and dry matter.
The water content is 99 percent of the total weight. He thinks they are too wet and puts them in an oven -
at low temperature - for them to lose some water.
At the output the water content is only 98%.
What is the total weight in kilograms (water content plus dry matter) coming out of the oven?
He finds 50 kilograms and he thinks he made a mistake: "So much weight lost for such a small change in water content!"
Can you help him?
Write function potatoes with
 - int parameter p0 - initial percent of water-
 - int parameter w0 - initial weight -
 - int parameter p1 - final percent of water -
potatoes should return the final weight coming out of the oven w1 truncated as an int.

Example:
potatoes(99, 100, 98) --> 50
'''

#First
def potatoes(p0, w0, p1):
    return int((round(w0 - (w0 / 100) * p0, 2) / (100 - p1) * 100)//1)

#Second
def potatoes2(p0, w0, p1):
    return w0 * (100 - p0) // (100 - p1)




print('1 result =', potatoes(82, 127, 80)) #114
print('2 result =', potatoes(93, 129, 91)) #100
print('3 result =', potatoes(84, 65, 80)) #52
print('4 result =', potatoes(93, 128, 92)) #112

