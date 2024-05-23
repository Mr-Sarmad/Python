# following are the higher order function (the function which takes an other function as an argument)
#MAP function
def cube(x):
    return x*x*x
l=[2,2,4,6,8,9,7]
newl=list(map(cube,l))
print(newl)
#so this the method of using map function

# FILTER FUNCTION

newnewl=list(filter(lambda x:x>2,l))
print(newnewl)
# this the method of using filter funtion  (it takes an argument in function and returns true and false.if it gives true the value will be add in the list,tupple or anyother iterable object )

#REDUCE FUNCTION

from functools import reduce

newnewnewl=reduce(lambda x,y: x+y,l)
print(newnewnewl)