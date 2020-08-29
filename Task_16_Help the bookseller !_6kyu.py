'''
A bookseller has lots of books classified in 26 categories labeled A, B, ... Z. Each book has a code c of 3, 4, 5 or
more characters. The 1st character of a code is a capital letter which defines the book category.
In the bookseller's stocklist each code c is followed by a space and by a positive integer n (int n >= 0) which
indicates the quantity of books of this code in stock.
For example an extract of one of the stocklists could be:

L = {"ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"}.
or
L = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"] or ....
You will be given a stocklist (e.g. : L) and a list of categories in capital
letters e.g :

  M = {"A", "B", "C", "W"}
or
  M = ["A", "B", "C", "W"] or ...

and your task is to find all the books of L with codes belonging to each
category of M and to sum their quantity according to each category.

For the lists L and M of example you have to return the string (in
Haskell/Clojure a list of pairs):

  (A : 20) - (B : 114) - (C : 50) - (W : 0)
where A, B, C, W are the categories, 20 is the sum of the unique book of
category A, 114 the sum corresponding to "BKWRK" and "BTSQZ", 50 corresponding
to "CDXEF" and 0 to category 'W' since there are no code beginning with W.

If L or M are empty return string is "" (Clojure should return an empty array
instead).

Note:
In the result codes and their values are in the same order as in M.

'''

#First:
def stock_list(listOfArt, listOfCat):
    coincidence_list = {}
    for i in range(len(listOfCat)):
        for j in range(len(listOfArt)):
            if listOfArt[j][0] ==  listOfCat[i]:
                if listOfCat[i] in coincidence_list:
                    coincidence_list[listOfCat[i]] += int(listOfArt[j].split(' ')[1])
                else:
                    coincidence_list[listOfCat[i]] = int(listOfArt[j].split(' ')[1])
            if listOfCat[i] not in coincidence_list:
                coincidence_list[listOfCat[i]] = 0
    if len(coincidence_list) == 0 or len(listOfArt) == 0 or len(listOfCat) == 0:
        coincidence_list = ''
        return coincidence_list
    end_list = []
    for k in range(len(listOfCat)):
        end_list.append("(" + listOfCat[k] + " : " + str(coincidence_list[listOfCat[k]]) + ")")
    return ' - '.join(end_list)



#Second:
from collections import Counter


def stock_list2(listOfArt, listOfCat):
    if (len(listOfArt) == 0) or (len(listOfCat) == 0):
        return ""
    codePos = listOfArt[0].index(' ') + 1
    cnt = Counter()
    for s in listOfArt:
        cnt[s[0]] += int(s[codePos:])
    return ' - '.join('({} : {})'.format(cat, cnt[cat]) for cat in listOfCat)




b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]

d = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
e = ["A", "B", "Y"]

f = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
g = []


print(stock_list(b, c))
print(stock_list(d, e))
print(stock_list(f, g))



print()
print('   and   ')
print()


print(stock_list2(b, c))
print(stock_list2(d, e))
print(stock_list2(f, g))
