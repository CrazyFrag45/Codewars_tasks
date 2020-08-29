'''
Robinson Crusoe decides to explore his isle. On a sheet of paper he plans the following process.
His hut has coordinates origin = [0, 0]. From that origin he walks a given distance d on a line
that has a given angle ang with the x-axis. He gets to a point A. (Angles are measured with respect to the x-axis)
From that point A he walks the distance d multiplied by a constant distmult on a line that has the angle ang
multiplied by a constant angmult and so on and on.
We have d0 = d, ang0 = ang; then d1 = d * distmult, ang1 = ang * angmult etc ...
Let us suppose he follows this process n times. What are the coordinates lastx, lasty of the last point?
The function crusoe has parameters;
n : numbers of steps in the process
d : initial chosen distance
ang : initial chosen angle in degrees
distmult : constant multiplier of the previous distance
angmult : constant multiplier of the previous angle
crusoe(n, d, ang, distmult, angmult) should return lastx, lasty as an array or a tuple depending on the language
Example:
crusoe(5, 0.2, 30, 1.02, 1.1) ->
The successive x are : 0.0, 0.173205, 0.344294, 0.511991, 0.674744, 0.830674 (approximately)
The successive y are : 0.0, 0.1, 0.211106, 0.334292, 0.47052, 0.620695 (approximately)
and
lastx: 0.8306737544381833
lasty: 0.620694691344071
Successive points:
x: 0.0, 0.9659..., 1.8319..., 2.3319..., 1.8319...
y: 0.0, 0.2588..., 0.7588..., 1.6248..., 2.4908...
Note
Please could you ask before translating: some translations are already written and published when/if the kata is
approved
'''

#First
from math import cos, sin, radians


def crusoe(n, d, ang, dist_mult, ang_mult):
    x, y = 0, 0
    for i in range(n):
        x += d * cos(radians(ang))
        y += d * sin(radians(ang))
        d *= dist_mult
        ang *= ang_mult
    return (x, y)

#Second
from math import cos, sin, radians

def crusoe2(n, d, ang, dist_mult, ang_mult):
    x, y, a = 0, 0, radians(ang)
    for i in range(n):
        x += d * cos(a)
        y += d * sin(a)
        d *= dist_mult
        a *= ang_mult
    return x, y




print('1 result =', crusoe(8, 0.22, 3, 1.01, 1.15)) #1.814652098870, 0.164646220964
print('2 result =', crusoe(29, 0.13, 21, 1.01, 1.09)) #0.318341393410, 2.292862212314
print('3 result =', crusoe(45, 0.10, 3, 1.01, 1.10)) #2.689897523779, 2.477953232467
print('4 result =', crusoe(14, 0.22, 20, 1.02, 1.14)) #1.774076472485, 2.557008479031
print('5 result =', crusoe(42, 0.11, 17, 1.02, 1.09)) #0.528555980656, 2.196434600133
