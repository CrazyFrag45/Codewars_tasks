'''Tower block is represented as *

Python: return a list;
for example, a tower of 3 floors looks like below

[
  '  *  ',
  ' *** ',
  '*****'
]
'''

#First var:
def tower_builder(n_floors):
    osnova = (n_floors * 2) - 1
    tower = []
    i = 1
    while i < n_floors:
        tow = (i * 2) - 1
        sky = ((osnova - tow) // 2)
        floor = str(sky * ' ') + str(tow * '*') + str(sky * ' ')
        tower.append(floor)
        i += 1
    tower.append(str(osnova * '*'))
    return tower

#Second var:
def tower_builder2(n_floors):
    return [("*" * (i*2-1)).center(n_floors*2-1) for i in range(1, n_floors+1)]



n_floors = 3


print(tower_builder(n_floors))
print(tower_builder2(n_floors))
