# Assignements in Python
x = 3
y = x
# x and y refer to the same object
print(id(x), id(y))
y = 2
print(id(x), id(y))



# Shallow vs Deep copy
x = [1, 2, 3]
y = x
y[0] = -11
# This changes x too! So make a copy before changing it
y = x[:]

''' This is only applicable for compound objects like nested lists
'''

import copy
x = [1, 2, [3, 4, 5]]
y = copy.copy(x)
# This only copies the elements in the outer lists (shallow copy)
y[2][0] = 0
# Changes the inner loop elemnts in x. Make a deep copy instead
y = copy.deepcopy(x)

'''
== vs is
== checks if values are same
is checks if the object is the same
'''
x is y  # False the id() of x and y are different
x == y  # True

# else if
if(1 > 2):
    pass
elif(1 == 2):
    print("They are equal")
else:
    print("2 is greater than 1")

# while
n = 5
while(n > 0):
    print(n)
    n -= 1

#for
for x in [1,2,3,4,5]:
    print(x)

for x in reversed([1,2,3,4,5]):
    print(x)

a = [1,2,3,4,5,6,7,8,9,10]
for i in range(0,10,2):
    print(a[i])

a.reverse() #Stick to reversed

for x in a:
    print(x)

#lists

dir(list) #Gives all operations that can be done on the list

a = [1,2,3,4,5,6,7,8,9,10]

a[0:11] # Slice of entier array

a[0:11:2] #Start from index 0 till index 11 in steps of 2

a[:-1] #Reverse the list

a[::2] #Increments of 2
